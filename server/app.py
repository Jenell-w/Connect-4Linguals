from flask import Flask, render_template, jsonify, session, request
import requests
from topicsAPI import topics_api
from authAPI import auth_api
from gameplayAPI import gameplay_api
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from harperdb_instance import url, headers
from helpers import find_game, update_board
import json


app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist"
            )
app.config['SECRET_KEY'] = 'ohsosecret0987654321'
app.secret_key = "@H238sd&ew9@#lso@Apso"
app.register_blueprint(topics_api)
app.register_blueprint(auth_api)
app.register_blueprint(gameplay_api)
socketio = SocketIO(app)

# this is for going directly to home

@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def catch_all(path):
    return(render_template('index.html'))

@app.after_request
def add_header(req):
    req.headers["Cache-Control"] = "no-cache"
    return req



#helper functions
def find_game(username):
    usernamesession = username
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

@socketio.on('gameboard')
def handle_item1(message, player):
    usernamesession = player
    updated_board = update_board(message)
    room = find_game(usernamesession)
    emit('gameboard',message, room=room)

@socketio.on('join')
def join(player):
    usernamesession = player
    room = find_game(usernamesession)
    join_room(room)
    emit('join_room', {'room': room, 'player': usernamesession})


if __name__ == "__main__":
    socketio.run(app, debug=True)

