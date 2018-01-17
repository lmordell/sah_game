# testing/test_game_api.py

""" Test API routes for the Game collection """

import unittest
from testing.utils import create_test_app

class GameTestCase(unittest.TestCase):
    """This class represents the Game test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        # Set up Flask App and Mongo DB
        create_test_app(self)

        self.player = {
            'nickname': 'player 1',
            'email': 'player1@fake_email.com'
        }

        self.game = {
            'uuid': '12345',
            'players': [
                {
                    'nickname': 'player 1',
                    'email': 'player1@fake_email.com'
                },
                {
                    'nickname': 'player 2',
                    'email': 'player2@fake_email.com'
                }
            ]
        }

    def tearDown(self):
        """ Destroy app and mongo connection """

    def test_create_game(self):
        """Test API can create a game (POST request)"""
        with self.app.test_request_context():
            res = self.client.post('/api/game', self.player)
            self.assertEqual(res.status_code, 201)
            self.assertIn('player 1', str(res.data))

    def test_get_game(self):
        """Test API can create a game (GET request)"""
        self.mongo.db.Game.insert(self.game)

        with self.app.test_request_context():
            res = self.client.get('/api/game/12345')
            self.assertEqual(res.status_code, 201)
            self.assertIn('12345', str(res.data))

    def test_delete_game(self):
        """Test API can delete an existing game. (DELETE request)."""
        with self.app.test_request_context():
            res = self.client.delete('/api/game/12345')
            self.assertEqual(res.status_code, 200)
            result = self.client.get('/api/game/12345')
            self.assertEqual(result.status_code, 404)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
