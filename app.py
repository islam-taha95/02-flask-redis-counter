import os
import redis
from flask import Flask
import time

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
secret_file = '/run/secrets/redis_password'

redis_password = None
if os.path.exists(secret_file):
    with open(secret_file, 'r') as f:
        redis_password = f.read().strip()

cache = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password
)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'👋 Hello from Flask! This page has been visited {count} times.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)