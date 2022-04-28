from flask import Flask, render_template, make_response, redirect
from flask_socketio import SocketIO, send, emit
import os

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/<name>')
def index(name):
    return render_template('index.html', name=name)

@socketio.on("message")
def handleMessage(data):
    emit("new_message",data,broadcast=True)

@socketio.on('connect')
def test_connect():
    emit("connected",broadcast=True)
    
if __name__ == "__main__":
    #socketio.run(app, port=8080, host='127.0.0.1')
    socketio.run(app)
