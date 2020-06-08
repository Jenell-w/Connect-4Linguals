from flask import Blueprint, jsonify, request, session
import requests
import json
from harperdb_instance import url, headers
from flask_socketio import SocketIO, emit

gameplay_api = Blueprint('gameplay_api', __name__)


def find_user_id(username):
    payload = {
        "operation": "sql",
        "sql": "SELECT id FROM ConnectLinguals.users where username = {}".format(username)
    }

    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload)).json()[0]
    return jsonify(success=True)


@gameplay_api.route('/enterword', methods=['GET', 'POST'])
def enter_word():
    username = session['user']
    current_user_id = find_user_id(username)
    print(current_user_id)

    playedword = request.json['item1Word']
    payload = {
        "operation": "insert",
        "schema": "ConnectLinguals",
        "table": "games",
        "records": [
            {
                "user_id": current_user_id,
                "played_word": playedword,

            }
        ]
    }
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))

    return jsonify(success=True)
    # how can we relate the user in session to the entered word.
