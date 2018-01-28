# app/api/game.py

""" Define routes and handlers for game creation, retrieval, and deletion """

###########
# Imports #
###########

import uuid
import json
import base64
from flask import request, Response
from app.database import MONGO as m
from . import API

##########
# Routes #
##########
@API.route('/game', methods=['POST'])
def create_game():
    """ Create a game instance & store in Mongo """

    # todo - create a session & store uuid in session (necesarry?)

    # Generate a UUID
    game_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes).replace('=', '')
    players = request.json['players']
    game = {
        'uuid': game_uuid,
        'players': players
    }
    m.db.Game.insert(game)
    return Response(json.dumps({'uuid': game_uuid, 'success': True}),
                    status=201,
                    mimetype='application/json')


@API.route('/game', methods=['GET'])
def get_game():
    """ Get a game instance from uuid query parameter """
    game_uuid = request.args['uuid']

    game = m.db.Game.find_one_or_404({'uuid': game_uuid}, {'_id': 0})
    return json.dumps(game)
