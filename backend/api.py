from datetime import datetime
import time
from flask import Flask
import requests
import json
from flask_cors import cross_origin
from flask import Blueprint
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)

@api.route('/time')
@cross_origin()
def get_current_time():
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    return {"time": formatted_now}

@api.route('/joke')
@cross_origin()
def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    random_joke = requests.get(url)
    print(random_joke)
    return json.loads(random_joke.text)

@api.route('/profile')
@jwt_required()
@cross_origin()
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body
