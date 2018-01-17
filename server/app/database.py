# app/database.py

""" Create a reference to MongoDB - it will be intialized in the API module """

from flask_pymongo import PyMongo

# Initialize MongoDB connection
MONGO = PyMongo()
