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


# @socketio.on('message')
# def handle_message(message):
#     send(message, broadcast=True)

@socketio.on('gameboard')
def handle_item1(message):
    usernamesession = session['user']
    room = find_game(usernamesession)
    updated_board = update_board(message)
    emit('gameboard',message, room=room)

@socketio.on('join')
def on_join(player2):
    usernamesession = session['user']
    room = find_game(usernamesession)
    join_room(room)
    send(usernamesession, room=room)
    send(player2, room=room)
    print('_________________________'+ player2 + ' has entered the room.  '+ room)
    print('_________________________'+ usernamesession + ' has entered the room.  '+ room)

#write the front end function to send data 
#to the join endpoint once a successful call
#is made to the db to create the game


if __name__ == "__main__":
    socketio.run(app, debug=True)

