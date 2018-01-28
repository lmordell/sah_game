# testing/test_game_api.py

""" Test API routes for the Game collection """

import json
from testing.util import FlaskPyMongoTest
from pprint import pprint

class GameTestCase(FlaskPyMongoTest):
    """This class represents the Game test case"""

    @classmethod
    def setUpClass(cls):
        """Define test variables"""
        super(GameTestCase, cls).setUpClass()
        cls.uuid = None
        cls.players = json.dumps({
            'players': [{
                'nickname': 'player 1',
                'email': 'player1@fake_email.com'
            }]
        })


    def test_create_game(self):
        """Test API can create a game (POST request)"""
        res = self.client.post('/api/game', data=self.players,
                               content_type='application/json',
                               follow_redirects=True)

        data = json.loads(res.data)

        self.__class__.uuid = data['uuid']

        self.assertEqual(res.status_code, 201)
        self.assertTrue(isinstance(data['uuid'], basestring))
        self.assertEqual(len(data['uuid']), 22)

    def test_get_game(self):
        """Test API can create a game (GET request)"""

        res = self.client.get('/api/game?uuid=' + self.uuid)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['players']), 2)
        self.assertEqual(data['uuid'], self.uuid)

    # def test_delete_game(self):
    #     """Test API can delete an existing game. (DELETE request)."""
    #     with self.app.test_request_context():
    #         res = self.client.delete('/api/game/12345')
    #         self.assertEqual(res.status_code, 200)
    #         result = self.client.get('/api/game/12345')
    #         self.assertEqual(result.status_code, 404)

