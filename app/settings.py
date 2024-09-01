from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure the database URI: replace 'sqlite:///transactions.db' with your database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

