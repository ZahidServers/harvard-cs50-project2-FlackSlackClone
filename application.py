import os

from flask import Flask, jsonify, render_template, request, redirect, url_for, abort, flash
from flask_socketio import emit, SocketIO
import json
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
channels=["lobby"]
messages = {"lobby": []}

@app.route("/")
def index():
    return redirect(url_for('channel', name='lobby'))
@app.route("/c/<string:name>")
def channel(name):
    if name not in channels:
        return "The channel {} does not exist.".format(name)
    return render_template("index.html", current_channel=name, channel_list=channels, messages=messages[name])
@socketio.on('message')
def handleMessage(msg):
    messages[msg["channel"]].append((msg["message"],msg["user"],msg["timestamp"]))
    print(messages)
    while(len(messages[msg["channel"]]) > 100):
        messages[msg["channel"]].pop(0)
    emit("messages",msg, broadcast=True)
@socketio.on("add channel")
def add_channel(data):
    print(data['channel'] + " has been recived")
    if data['channel'] not in channels:
        print("channel is unique")
        channels.append(data['channel'])
        print(channels)
        messages.setdefault(data['channel'], [])
        print(messages)
        emit("add channel", {"channel": data['channel']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)