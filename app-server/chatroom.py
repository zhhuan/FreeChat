from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect


async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

@app.route('/')
def index():
	return render_template('login.html')


@socketio.on('connect',namespace='/chatroom')
def test_connect():
	print('a user connected')


@socketio.on('send_msg', namespace='/chatroom')
def test_message(message):
	emit('pub_msg',{'data':message['data']},broadcast=True)


if __name__ == '__main__':
	socketio.run(app,debug=True)