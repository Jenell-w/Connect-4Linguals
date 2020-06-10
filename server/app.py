from flask import Flask, render_template, jsonify
import requests
from topicsAPI import topics_api
from authAPI import auth_api
from flask_socketio import SocketIO, send

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist"
            )
app.secret_key = "@H238sd&ew9@#lso@Apso"
app.register_blueprint(topics_api)
app.register_blueprint(auth_api)
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

@socketio.on('message')
def handle_message(message):
    send(message, broadcast=True)

@socketio.on('item1')
def handle_item1(message):
    send(message, broadcast=True)
    print('Item SENT__________________', message)

if __name__ == "__main__":
    socketio.run(app, debug=True)
