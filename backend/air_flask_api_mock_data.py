# sudo pip install flask
# FLASK_APP=air_flask_api_mock_data flask run --host=0.0.0.0

from flask import Flask, jsonify
import json
import airly_api_fetch as airly_api_fetch
app = Flask(__name__)


@app.route("/")
def air():
    response = jsonify([
        {
            "address": "Kordeckiego 9", 
            "air": {
                        "airPressure": 1019.0, 
                        "aqi": {
                            "value": 20,
                            "color": "#6BC926"
                        }, 
                        "humidity": 73.24, 
                        "temperature": 10.4
                    }
        }, 
        {   
            "address": "Slowackiego 44", 
            "air": {
                       "airPressure": 1018.89, 
                        "aqi": {
                            "value": 20,
                            "color": "#6BC926"
                        },
                       "humidity": 76.3, 
                       "temperature": 9.92
                    }
        }, 
        {
            "address": "Puszkarska 7j",
            "air": {
                        "airPressure": 1017.64, 
                        "aqi": {
                            "value": 20,
                            "color": "#6BC926"
                        },
                        "humidity": 79.99, 
                        "temperature": 11.43
                    }
            }
    ])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
