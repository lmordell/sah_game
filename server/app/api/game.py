# app/api/game.py

""" Define routes and handlers for game creation, retrieval, and deletion """

###########
# Imports #
###########

from flask import request, jsonify
from . import API
from app.database import MONGO as m

##########
# Routes #
##########

@API.route('/game', methods=['POST'])
def create_game():
    """ Create a game instance & store in Mongo """
    # Generate a UUID (TODO actually generate)
    uuid = request.get('uuid')
    players = request.get('players')
    game = {
        'uuid': uuid,
        'players': players
    }
    res = m.db.Game.insert(game)
    return jsonify(res)

