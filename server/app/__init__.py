# app/__init__.py

""" Initialize main App module """

###########
# Imports #
###########

import os
from flask import Flask, jsonify

from app.config import APP_CONFIG

###########
# Methods #
###########

def create_app(config_name):
    """ Create an instance of the Flask app """
    app = Flask(__name__)
    app.config.from_object(APP_CONFIG[config_name])
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    return app

def register_blueprints(app):
    """ Register imported blueprints """
    app.register_blueprint(API)
    return None

##############################
# Create App & DB Connection #
##############################

CONFIG_NAME = os.getenv('APP_SETTINGS')

# Create the app
APP = create_app(CONFIG_NAME)

from app.api import API

# Register Blueprints
register_blueprints(APP)
