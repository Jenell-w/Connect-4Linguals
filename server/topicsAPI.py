from flask import Blueprint, jsonify, request, session
import requests
import json
from harperdb_instance import url, headers

topics_api = Blueprint('topics_api', __name__)


@topics_api.route('/gettopics', methods=['POST'])
def get_topics():
    # returns the list of topics
    payload = "{\n  \"operation\": \"sql\",\n  \"sql\":\"SELECT topics FROM ConnectLinguals.topics\"\n}"
    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text.encode('utf8')


@topics_api.route('/addtopic', methods=['POST'])
def add_topic():
    # add user-entered topic to table in db
    topic = request.json["topic"]
    payload = {
        "operation": "insert",
        "schema": "ConnectLinguals",
        "table": "topics",
        "records": [
            {
                "topics": topic
            }
        ]
    }
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))

    return jsonify(success=True)
