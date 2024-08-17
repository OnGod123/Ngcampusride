# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Gunicorn will run on
EXPOSE 8000

# Set environment variables (optional)
ENV FLASK_ENV=production

# Command to run Gunicorn server with your configuration file
CMD ["gunicorn", "-c", "gunicorn.py", "main:app"]

