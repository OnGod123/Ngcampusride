# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code
COPY app /app

# Command to run Gunicorn with the Flask app
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app.app:app"]
