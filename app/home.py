from settings import app, db  # Assuming these are in settings.py

# Other necessary imports
from flask import Flask

# If you have models or routes in other modules, import them as well
from pay_wall.pay_verification import response  # Example of importing a function
from pay_wall.pay_wall_server import initialize_payment  # Example of importing a route




@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000, debug=True)
