# testing/test_list_api.py

""" Test API routes for the List collection """

import json
from bson.json_util import dumps
from testing.util import FlaskPyMongoTest

class ListTestCase(FlaskPyMongoTest):
    """This class represents the Game test case"""

    @classmethod
    def setUpClass(cls):
        """Define test variables"""
        super(ListTestCase, cls).setUpClass()

        # Create test game
        cls.mongo.db.Game.insert({
            'uuid': '1234',
            'players': [{
                'nickname': 'player 1',
                'email': 'player1@sah_game.com'
            }],
            'used_lists': []
        })

        # Insert a test list
        cls.mongo.db.List.insert({
            'name': 'test_list',
            'questions': ['question 1', 'question 2', 'question 3']
        })

    def test_get_list(self):
        """Test API can get a random list (GET request)"""

        # **** TODO ****
        # res = self.client.get('/api/list?uuid=1234')
        # data = json.loads(res.data)
        # self.assertEqual(data['name'], 'test_list', msg='Returns a list')
        # self.assertEqual(len(data['questions']), 3, msg='Returns 3 questions')

    def test_get_used_list(self):
        """Test API throws an error when attempting to get a used list (GET request)"""

        # **** TODO ****
        # res = self.client.get('/api/list?uuid=1234')
        # self.assertEqual(res.status_code, 404, msg='Returns 404 error')
