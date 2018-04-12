# testing/util.py

""" Utility classes for creating flask test app and mongoDB testing connection """

import os
import unittest
import uuid
import flask_pymongo
from app import APP

class FlaskRequestTest(unittest.TestCase):
    """Set up the flask testing application"""

    @classmethod
    def setUpClass(cls):
        cls.app = APP
        cls.client = APP.test_client()
        cls.context = cls.app.test_request_context('/')
        cls.context.push()

    @classmethod
    def tearDownClass(cls):
        cls.context.pop()

class FlaskPyMongoTest(FlaskRequestTest):
    """Set up the connection to the test mongo DB"""

    @classmethod
    def setUpClass(cls):
        super(FlaskPyMongoTest, cls).setUpClass()

        # Generate a unique config prefix for each test
        config_prefix = uuid.uuid4()
        cls.mongo = flask_pymongo.PyMongo(cls.app, config_prefix=config_prefix)

    @classmethod
    def tearDownClass(cls):

        # Remove all data from the db
        cls.mongo.cx.drop_database(os.getenv('MONGO_DBNAME'))

        super(FlaskPyMongoTest, cls).tearDownClass()
