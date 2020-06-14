from flask import Flask, render_template, jsonify, session
import requests
from topicsAPI import topics_api
from authAPI import auth_api
from gameplayAPI import gameplay_api
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from harperdb_instance import url, headers
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


@socketio.on('message')
def handle_message(message):
    send(message, broadcast=True)

@socketio.on('gameboard')
def handle_item1(message):
    usernamesession = session['user']
    room = find_game(usernamesession)
    update_board = update_board(message)
    send(update_board, room=room)
    print('Item SENT__________________', message, usernamesession, room)

@socketio.on('join')
def on_join():
    usernamesession = session['user']
    room = find_game(usernamesession)
    join_room(room)
    send(usernamesession + ' has entered the room.', room=room)

#write the front end function to send data 
#to the join endpoint once a successful call
#is made to the db to create the game


if __name__ == "__main__":
    socketio.run(app, debug=True)

