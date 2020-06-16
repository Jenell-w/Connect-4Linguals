from flask import Flask, render_template, jsonify, session, request
import requests
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from harperdb_instance import url, headers
import json

#helper functions
def find_game(username):
    usernamesession = session['user']
    username_values = ["Player2_username", "Player1_username"]
    game_id = 'nogame'
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
            game_id = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()[0]['id']
    return game_id

def update_board(board):
    usernamesession = session['user']
    game = find_game(usernamesession)
    boardtostring = '[ '+ ', '.join(board)+ ' ]'
    print(boardtostring)
    payload = {
            "operation":"update",
            "schema":"ConnectLinguals",
            "table":"games",
            "records": [
                {
                    "id": "{}".format(game),
                    "board": "{}".format(boardtostring)
                },
            ]
        }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()
    return response
