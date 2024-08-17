# gunicorn.py
bind = '0.0.0.0:8000'  # Bind to all network interfaces on port 8000
workers = 4  # Number of worker processes to handle requests

# Optional: Additional configurations
worker_class = 'gevent'  # Use gevent for asynchronous workers (optional)
timeout = 30  # Timeout for workers (optional)

