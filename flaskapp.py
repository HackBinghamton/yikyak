import json
from flask import Flask, request
app = Flask(__name__)

yaks = [
        {'text': 'Hello world', 'votes': 5},
        {'text': 'This is a yak', 'votes': -2}
        ]


@app.route("/", methods=['GET'])
def mainpage():
    return app.send_static_file('index.html')


@app.route("/yak", methods=['POST'])
def addyak():
    yaks.insert(0, request.get_json())
    return "okay"


@app.route("/yaks", methods=['GET'])
def getyaks():
    return json.dumps(yaks)


@app.route("/upvote", methods=['POST'])
def upvote():
    yak = request.get_json()['id']
    yaks[yak]['votes'] += 1
    return "okay"


@app.route("/downvote", methods=['POST'])
def downvote():
    yak = request.get_json()['id']
    yaks[yak]['votes'] -= 1
    return "okay"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
