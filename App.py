from flask import Flask, request
import os, sys
from USE import USE
from STT import STT

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/init2')
def init():
    return 'asdf'

@app.route("/question")
def question():
    return USE(request.args.get('question'))

@app.route("/STT")
def speech_to_text():
    return STT(request.args.get('speech'))

if __name__ == '__main__':
    app.run(debug=True)