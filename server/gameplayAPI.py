from flask import Blueprint, jsonify, request, session, g
import requests
import json
from harperdb_instance import url, headers
from flask_socketio import SocketIO, emit
from helpers import find_game, update_board

gameplay_api = Blueprint('gameplay_api', __name__)

@gameplay_api.route('/userlist', methods=['GET', 'POST'])
def get_all_users():
    currentuser = session['user']
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
    cleaned_username_list = res = [i for i in username_list if not (i['username'] == currentuser)] 
    return jsonify(cleaned_username_list)


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
    player1_in_session = session['user']
    player2_selected = request.json['player']
    board = "[ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "" ]"
    official_game_topic = request.json['officialGameTopic']
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


@gameplay_api.route('/checkifingame', methods=['POST', 'GET'])
def checkifgame():
    usernamesession = session['user']
    username_values = ["Player2_username", "Player1_username"]
    game_id = {'game':'nogame'}
    for name in username_values:
        payload = {
            "operation":"search_by_value",
            "schema":"ConnectLinguals",
            "table":"games",
            "search_attribute":name,
            "search_value":"{}".format(usernamesession),
            "get_attributes": ["*"]
        } 
        if requests.request("POST", url, headers=headers, data=json.dumps(payload)).json() != []:
            game_id = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()[0]
    return jsonify(success = game_id)

@gameplay_api.route('/userchallenge', methods=['POST', 'GET'])
def update_challenges():
    usernamesession = session['user']
    game = find_game(usernamesession)
    challenge_reason = request.json['reason']
    print(challenge_reason)
    comment = request.json['challengeComment']
    print(comment)
    payload = {
            "operation":"update",
            "schema":"ConnectLinguals",
            "table":"games",
            "records": [
                {
                    "id": "{}".format(game),
                    "challenge_reason": challenge_reason,
                    "challenge_comments": comment
                },
            ]
        }
    try: 
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()[0]
    except:
        print('no value found')
    return jsonify(success=True)