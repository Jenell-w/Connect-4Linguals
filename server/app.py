from flask import Flask, render_template, jsonify
import requests
from topicsAPI import topics_api
from harperdb_instance import response
from authAPI import auth_api

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist"
            )
app.secret_key = "@H238sd&ew9@#lso@Apso"
app.register_blueprint(topics_api)
app.register_blueprint(auth_api)

@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def catch_all(path):
        return render_template("index.html")
    

@app.after_request
def add_header(req):
    """
    Clear cache for hot-reloading
    """
    req.headers["Cache-Control"] = "no-cache"
    return req


if __name__ == "__main__":
    app.run(debug=True)
