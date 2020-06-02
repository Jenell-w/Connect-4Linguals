# try to connect the db to the project -- need to call for
# random topics to appear from db.   How to add the sql commands?
from flask import Blueprint, jsonify, request, session
import requests
import json
from harperdb_instance import response, url, headers

topics_api = Blueprint('topics_api', __name__)


@topics_api.route('/gettopics', methods=['GET', 'POST'])
def get_topics():
    # returns the list of topics!!
    return response.text.encode('utf8')


# @topics_api.route('addtopic', methods=['POST'])
# def add_topic():
