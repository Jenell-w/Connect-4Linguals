from flask import Blueprint, jsonify, request, session
import requests
import json
from harperdb_instance import response, url, headers


auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/login', methods=['GET', 'POST'])
def login():
  payload = '''{
	"operation":"insert",
	"schema":"ConnectLinguals",
	"table":"users",
	"records": [
      {
        "username" : "Pete",
        "pass": "XXXXXXX"
      }
    ]
}'''
  response = requests.request("POST", url, headers=headers, data=payload)
  return response.text.encode('utf8')