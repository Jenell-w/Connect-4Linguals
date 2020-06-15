from flask import Flask, render_template, jsonify, session
import requests
from harperdb_instance import url, headers

def find_game(username):
    username_values = ["Player1_username","Player2_username"]
    game_id = ''
    for name in username_values:
        payload = {
            "operation":"search_by_value",
            "schema":"ConnectLinguals",
            "table":"games",
            "search_attribute":name,
            "search_value":"{}".format(username),
            "get_attributes": ["*"]
        } 
        try: 
            game_id = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()[0]['id']
        except:
            print('no value found')
    return game_id

def update_board(board):
    usernamesession = session['user']
    game = find_game(usernamesession)
    payload = {
            "operation":"update",
            "schema":"ConnectLinguals",
            "table":"games",
            "records": [
                {
                    "id": "{}".format(game),
                    "board": "{}".format(board)
                },
            ]
        }
    try: 
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()[0]['board']
    except:
        print('no value found')
    return response
