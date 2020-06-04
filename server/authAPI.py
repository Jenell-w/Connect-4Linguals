from flask import Blueprint, jsonify, request, session
import requests
import json
from harperdb_instance import url, headers
import bcrypt

auth_api = Blueprint('auth_api', __name__)

def find_if_user_name_exists(username):
  payload = {
	"operation":"search_by_value",
	"schema":"ConnectLinguals",
	"table":"users",
	"search_attribute":"username",
	"search_value":"{}".format(username),
	"get_attributes": ["*"]
  }
  try: 
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()[0]
  except IndexError:
    return "False"
  return "True"

@auth_api.route('/login', methods=['GET', 'POST'])
def login():
  session['user'] = ''
  password = request.json["password"].encode('UTF-8')
  username = request.json["username"]
  payload = {
	"operation":"search_by_value",
	"schema":"ConnectLinguals",
	"table":"users",
	"search_attribute":"username",
	"search_value":"{}".format(username),
	"get_attributes": ["*"]
  }
  hashed = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()[0]['pass']
  if bcrypt.checkpw(password, hashed.encode('UTF-8')):
    session['user'] = username
    usernamesession = session['user']
    return jsonify(session=usernamesession)
  else:
    return jsonify(success=False)


@auth_api.route('/register', methods=['GET', 'POST'])
def register():
  session['user'] = ''
  username = request.json["username"]
  if find_if_user_name_exists(username) == "True":
    return "Name Already Exists"
  password = request.json["password"].encode('UTF-8')
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())
  decoded_hashed = hashed.decode('utf8')
  payload = {
    "operation":"insert",
    "schema":"ConnectLinguals",
    "table":"users",
    "records": [
        {
          "username" : username,
          "pass": "{}".format(decoded_hashed)
        }
      ]
  }
  response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
  session['user'] = username
  usernamesession = session['user']
  return jsonify(session=usernamesession)


@auth_api.route('/checksession', methods=["GET"])
def check_session():
        if 'user' in session:
                return jsonify(
                        session = True,
                        user = session['user']
                )
        else:
                return jsonify(session = False)