from flask import Blueprint, jsonify, request, session, g
import requests
import json
from harperdb_instance import url, headers
from flask_socketio import SocketIO, emit

gameplay_api = Blueprint('gameplay_api', __name__)

@gameplay_api.route('/userlist', methods=['GET', 'POST'])
def get_all_users():
    payload = {
        "operation": "search_by_value",
        "schema": "ConnectLinguals",
        "table": "users",
        "search_attribute": "username",
        "search_value": "*",
        "get_attributes": ["username"]
    }
    username_list = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload)).json()
    return jsonify(username_list)


@gameplay_api.route('/currentplayerlist', methods=['GET', 'POST'])
def get_players_in_games():
    payload = {
        "operation": "search_by_value",
        "schema": "ConnectLinguals",
        "table": "games",
        "search_attribute": "Player1_username",
        "search_value": "*",
        "get_attributes": ["Player1_username", "Player2_username"]
    }
    players_active = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload)).json()
    return jsonify(players_active)

@gameplay_api.route('/startgame', methods=['POST', 'GET'])
def get_gameboard_started():
    # if board is not empty, retrieve game_id and players
    player1_in_session = session['user']
    print(player1_in_session)
    player2_selected = request.json['player']
    print(player2_selected)
    board = "[ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "" ]"
    official_game_topic = request.json['officialGameTopic']
    print(official_game_topic)
    payload = {
        "operation": "insert",
        "schema": "ConnectLinguals",
        "table": "games",
        "records": [
            {
                "Player1_username": player1_in_session,
                "Player2_username": player2_selected,
                "board": board,
                "official_game_topic": official_game_topic,
                "winner": ""
            }
        ]
    }
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))
    return jsonify(success=True)

