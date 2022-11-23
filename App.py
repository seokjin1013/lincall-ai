from flask import Flask, request
from USE import USE
from STT import STT
from SA import SA
from Summary import Summary

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/question")
def question():
    return USE(request.args.get('question'))

@app.route("/STT")
def speech_to_text():
    return STT(request.args.get('speech'))

@app.route("/sentiment")
def sentiment_analysis():
    return SA(request.args.get('sentence'))

@app.route("/summary")
def summary():
    return Summary(request.args.get('sentence'))

if __name__ == '__main__':
    app.run(debug=True)