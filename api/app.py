from datetime import datetime
import time
from flask import Flask
import requests
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/time')
@cross_origin()
def get_current_time():
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    return {"time": formatted_now}

@app.route('/joke')
@cross_origin()
def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    random_joke = requests.get(url)
    print(random_joke)
    return json.loads(random_joke.text)
