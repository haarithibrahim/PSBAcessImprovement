from flask import Flask, request, jsonify  # Import Flask and useful tools
from flask_sqlalchemy import SQLAlchemy     # Import SQLAlchemy for database management
from datetime import datetime               # Import datetime for handling dates and times

app = Flask(__name__)  # Create an instance of the Flask app

# Configuring the SQLAlchemy Database URI for MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/PSB_STUDENT'
db = SQLAlchemy(app)  # Initialize SQLAlchemy with the Flask app
