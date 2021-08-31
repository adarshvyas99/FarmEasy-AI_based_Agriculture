
import requests
import json
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key = 'a'

@app.route('/')
def home():
    return render_template('index.html')

 
API_KEY = "GewCq7UyzLLYh-bXcEZfrHqF4ynQb-7hVwCWG5rBTRXx"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True, port=9000)