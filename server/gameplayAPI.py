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

# could i query without the user in session? why does WHERE NOT not work?
# do i need to find current user in sessino first?
@gameplay_api.route('/playerlist', methods=['GET', 'POST'])
def get_avail_players():
    user_in_session = session['user']
    print('-----------', user_in_session)
    payload = {
        "operation": "sql",
        "sql": "SELECT username FROM ConnectLinguals.users"

    }
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))
    username_list = response.text.encode('utf8')
    payload = {
        "operation": "search_by_value",
        "schema": "ConnectLinguals",
        "table": "games",
        "search_attribute": "Player1_username",
        "search_value": "*",
        "get_attributes": ["Player1_username", "Player2_username"]
    }
    response2 = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))
    players_playing = response2.text.encode('utf8')
    # thisis returning 2 arrays next to each other, how can we make them together as 1 array

    return (username_list + players_playing)

    # how can we relate the user in session to the entered word.
