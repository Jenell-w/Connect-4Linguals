from flask import Flask, render_template, jsonify
import requests
from topicsAPI import topics_api
from harperdb_instance import response

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist"
            )
app.register_blueprint(topics_api)


@app.route("/")
def serve_vue_app():
    """
    serve our Vue app
    """
    return(render_template('index.html'))


@app.after_request
def add_header(req):
    """
    Clear cache for hot-reloading
    """
    req.headers["Cache-Control"] = "no-cache"
    return req


if __name__ == "__main__":
    app.run(debug=True)
