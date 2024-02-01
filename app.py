from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Initialize a list to store messages
messages = []

@app.route('/')
def sessions():
    return render_template('session.html')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    # Append the received message to the messages list
    messages.append(json)
    # Emit the message to all clients, including the sender
    socketio.emit('my response', json)

@socketio.on('connect')
def on_connect():
    # Emit all previous messages to the just-connected client
    for message in messages:
        socketio.emit('my response', message, to=request.sid)

if __name__ == '__main__':
    socketio.run(app, debug=True)