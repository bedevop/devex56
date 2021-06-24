from flask import Flask, redirect, request

app = Flask(__name__)


@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    if request.method == 'GET':
        #a = 1/0
        return '<font size=7>My name is Aviel</font>'
    elif request.method == 'POST':
        return 'creating your name'


app.run(host="0.0.0.0", port=5001, debug=True)