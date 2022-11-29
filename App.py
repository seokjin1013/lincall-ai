from flask import Flask, request
from USE import USE
from STT import STT
from SA import SA
from Summary import Summary
from Keyword import Keyword
from Wordcloud import Wordcloud

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/question")
def question():
    return USE(request.args.get('sentence'))

@app.route("/STT")
def speech_to_text():
    open('tmp_speech.wav', 'wb').write(request.args.get('speech'))
    return STT('tmp_speech.wav')

@app.route("/sentiment")
def sentiment_analysis():
    return SA(request.args.get('sentence'))

@app.route("/summary")
def summary():
    return Summary(request.args.get('sentence'))

@app.route("/wordcloud")
def wordcloud():
    sentence = request.args.get('sentence')
    theme = request.args.get('theme')
    return Wordcloud(sentence, theme)

@app.route("/keyword")
def keyword():
    return Keyword(request.args.get('sentence'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3389)