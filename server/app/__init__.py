# app/__init__.py

import os
from flask import Flask, jsonify
import pymongo

# instantiate the app
app = Flask(__name__)

# set config
app.config.from_object('app.config.DevelopmentConfig')
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# set up mongo DB env vars
# app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# client = pymongo.MongoClient(app.config['MONGO_URI'])
# db = client.cah

# # instantiatce mongo DB
# # mongo = PyMongo(app)
# inserted = db.cah_demo.insert_one({ "work": True, "awesome": "yes" })

# print(inserted)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })