from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

import pymysql.cursors
from pymysql.err import IntegrityError

async_mode = None

app = Flask(__name__,static_url_path='',static_folder='../app-client/dist')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

connection = pymysql.connect(host='localhost',
							 user='johan',
							 password='AlarmJohan',
							 db='free_talk',
							 charset='utf8')

@app.route('/')
def index():
	return app.send_static_file('index.html')


@socketio.on('connect',namespace='/chatroom')
def test_connect():
	print('a user connected')


@socketio.on('send_msg', namespace='/chatroom')
def test_message(message):
	emit('pub_msg',{'data':message['data']},broadcast=True)

@socketio.on('validator_user', namespace='/validator')
def validator_user(msg):
	username = msg['data']
	try:
		with connection.cursor() as cursor:
			sql = "SELECT `chat_user` FROM `dat_user` WHERE `chat_user` = %s"
			cursor.execute(sql, (username))
			result = cursor.fetchone()
			if result:
				emit('exist_user',{'data':1})
			else:
				emit('exist_user',{'data':0})

		connection.commit()

	finally:
		print('search done')
		# connection.close()
	
@socketio.on('login_room', namespace='/validator')
def login_room(msg):
	username = msg['username']
	password = msg['password']
	try: 
		with connection.cursor() as cursor:
			sql = "SELECT `chat_pwd` FROM `dat_user` WHERE `chat_user` = %s"
			cursor.execute(sql, (username))
			result = cursor.fetchone()
			if password in result:
				emit('login_done',{'data':1})
			else:
				emit('login_done',{'data':0})
	finally:
		print('check done')

@socketio.on('register_user',namespace='/register')
def register_user(msg):
	user = msg['user']
	password = msg['pwd']
	email = msg['email']
	print(user,password,email)
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO `dat_user`(`chat_user`,`chat_pwd`,`chat_email`) VALUES (%s,%s,%s)"
			cursor.execute(sql,(user,password,email))
		
		connection.commit()
	except IntegrityError as e:
		print('IntegrityError:',e)
		emit('register_done',{'data':0})
	else:
		emit('register_done',{'data':1})
	finally:
		print('done')

if __name__ == '__main__':
	# socketio.run(app,host='192.168.0.189',port=10000)
	socketio.run(app, debug=True)