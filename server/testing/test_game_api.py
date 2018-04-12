# testing/test_game_api.py

""" Test API routes for the Game collection """

import json
from testing.util import FlaskPyMongoTest

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

        self.assertEqual(res.status_code, 201, msg='Creates game')
        self.assertIsInstance(data['uuid'], basestring, msg='Generates uuid')
        self.assertEqual(len(data['uuid']), 22, msg='uuid has 22 characters')

    def test_get_game(self):
        """Test API can create a game (GET request)"""

        res = self.client.get('/api/game?uuid=' + self.uuid)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200, msg='Gets game')
        self.assertEqual(len(data['players']), 1, msg='Returns a single player')
        self.assertEqual(data['uuid'], self.uuid, msg='Returns the correct uuid')
