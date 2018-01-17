# app/api/__init__.py

""" Initialize app API module """

from flask import Blueprint
from app import APP
from app.database import MONGO

# Initialize the DB
MONGO.init_app(APP)

# Create API blueprint
API = Blueprint('api', __name__, url_prefix='/api')

# Import API Files
from . import game
from . import list
