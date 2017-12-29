<!DOCTYPE html>
<html>
<head>
	<title>johan's chatroom</title>
	<link rel="stylesheet" type="text/css" href="{{ url_for('static',filename='style.css') }}">
</head>
<body>
	<div id="chatroom">
		<div id="roomName">test room</div>
		<div id="chatContent">
			<ul id="chatRecords"></ul>
		</div>
		<div id="writeZone">
			<input id="sendMsg" type="text" name="myTalk">
			<button id="sendBtn">Send</button>
		</div>
	</div>
</body>

<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.5/socket.io.min.js"></script>
<script type="text/javascript">

    namespace = '/chatroom';

	var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace)
	

	var sendBtn = document.getElementById('sendBtn');
	sendBtn.onclick = function () {
		var sendMsg = document.getElementById('sendMsg').value;
		socket.emit('send_msg',{data:sendMsg});
	}

	var chatRecords = document.getElementById('chatRecords');
	socket.on('pub_msg', function(msg){
		var wordHtml = '<li class="msg">'+msg.data+'</li>'
		chatRecords.insertAdjacentHTML('beforeEnd',wordHtml)
	})
</script>
</html>