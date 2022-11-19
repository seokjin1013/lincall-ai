from flask import Flask, request
import os, sys
import USE

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/init2')
def init():
    
    return 'asdf'

@app.route("/question", methods = ['POST'])
def question():
    params = request.get_json()
    return USE(params['question'])

if __name__ == '__main__':
    app.run(debug=True)