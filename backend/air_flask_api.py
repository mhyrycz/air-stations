# sudo pip install flask
# FLASK_APP=air_flask_api flask run --host=0.0.0.0

from flask import Flask, jsonify
import json
import airly_api_fetch as airly_api_fetch
app = Flask(__name__)


@app.route("/")
def air():
    response = jsonify(airly_api_fetch.get_air_params())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
