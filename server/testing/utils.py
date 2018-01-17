# testing/utils.py

""" Utility methods for running unit tests """

import os
from app import create_app, init_db

def create_test_app(self):
    """ Set a test Flask app and MongoDB on the test class """
    self.app = create_app(config_name="testing")

    # Set the test context
    self.client = self.app.test_client()
    self.mongo = init_db(self.app, os.getenv('MONGO_TEST_URI'))

# TODO: Destroy test app on tearDown?

# TODO: Make a 'make_request' helper method to mock API requests
# def make_request(self, endpoint, method, data):
# 	with self.app.test_request_context():
# 		return self.client[method](endpoint, data=data)
