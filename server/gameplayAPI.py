from flask import Blueprint, jsonify, request, session
import requests
import json
from harperdb_instance import url, headers

gameplay_api = Blueprint('gameplay_api', __name__)


@gameplay_api.route('/enterword', methods=['POST'])
def enter_word():
    playedword = request.json['playedword']
    # how can we relate the user in session to the entered word.
    # how can we relate the game play to which game is in session
    # link active game with the current game board.
