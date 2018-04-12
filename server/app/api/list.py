# app/api/list.py

""" Define routes and handlers for list retrieval """

###########
# Imports #
###########
from bson.json_util import dumps
from flask import request, Response
from app.database import MONGO as m
from . import API

##########
# Routes #
##########
@API.route('/list', methods=['GET'])
def get_list():
    """ Get an unused random list """
    uuid = request.args.get('uuid')

    game = m.db.Game.find_one_or_404({'uuid': uuid}, {'used_lists': 1})

    # Get and parse the list
    game_list = m.db.List.find_one_or_404({"name":{'$nin': game.get('used_lists') or []}})
    parsed_list = dumps(game_list)

    # Add the list name to used_lists array
    m.db.Game.update({'uuid': uuid}, {'$push':{'used_lists': game_list.get('name')}})

    return Response(parsed_list, status=200, mimetype='application/json')
