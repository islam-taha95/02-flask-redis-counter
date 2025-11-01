# Using an official Python image
FROM python:3.10-slim

# Setting working directory inside the container
WORKDIR /app

# Installing python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the app files
COPY . .

# Expose the Flask port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
