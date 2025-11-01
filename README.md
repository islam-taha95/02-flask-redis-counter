# 🚀 Flask + Redis Counter App (with Docker Swarm & Secrets)

This project demonstrates a **Flask web application** that connects to a **Redis database** to count page visits.  
It’s deployed securely using **Docker Swarm**, **Docker Secrets**, and **named volumes** for persistence.

---

## 📁 Project Structure
02-flask-redis-counter/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
└── secrets/
└── redis_password.txt

---

## 🧱 Components
- **Flask (Python)** – serves a simple web app with a counter.
- **Redis (Alpine)** – stores the visit count.
- **Docker Secrets** – securely stores the Redis password.
- **Docker Swarm** – orchestrates and isolates services.

---

## ⚙️ Setup Instructions

1️⃣ Clone the repo
```bash
git clone https://github.com/<your-username>/02-flask-redis-counter.git
cd 02-flask-redis-counter
2️⃣ Create a Redis password secret
mkdir -p secrets
echo "myStrongRedisPass123" > secrets/redis_password.txt
3️⃣ Initialize Docker Swarm (if not already)
docker swarm init
4️⃣ Create the Docker secret
docker secret create redis_password ./secrets/redis_password.txt
5️⃣ Build the Flask image
Docker Swarm doesn’t support build: directives, so build manually.
docker build -t flask-redis-app:latest .
6️⃣ Deploy the stack
docker stack deploy -c docker-compose.yml flask-redis-stack
🌍 Access the Application
The app runs on port 8080, not 5000.
Port 5000 is often used by macOS system processes (e.g., ControlCenter),
which can cause port binding conflicts.
We expose Flask on port 8080 instead.
Visit:
http://localhost:8080
Expected output:
👋 Hello from Flask! This page has been visited 1 times.
🧩 Useful Docker Commands
Check running services:
docker service ls
View logs:
docker service logs flask-redis-stack_web
Remove stack:
docker stack rm flask-redis-stack
List secrets:
docker secret ls
🛡️ Security Notes
Redis password is not hardcoded — it’s managed via Docker Secrets.
Secrets are mounted only inside containers under /run/secrets/.
Never commit secrets/redis_password.txt to Git.
