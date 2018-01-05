<template>
	<div id="chatroom">
		<div id="roomName">test room</div>
		<div id="chatContent">
			<ul id="chatRecords"></ul>
		</div>
		<div id="writeZone">
			<input v-model="sendMsg" type="text" name="myTalk">
			<button v-on:click="sendTalk">Send</button>
		</div>
	</div>
</template>
  
<script>
	import io from 'socket.io-client'

	var namespace = '/chatroom'
	var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace)
	
	socket.on('pub_msg',function(msg){
		var chatRecords = document.getElementById('chatRecords')
		var wordHtml = '<li class="msg">'+msg.data+'</li>'
		chatRecords.insertAdjacentHTML('beforeEnd',wordHtml)
	})

	export default {
		data: function(){
			return {sendMsg:'test'}
		},
		methods: {
			sendTalk: function() {
				socket.emit('send_msg',{data:this.sendMsg})
			}
		}
	}
</script>

<style>
	#roomName {
		text-align: center;
	}

	#chatContent {
		width: 20rem;
		min-height: 10rem;
		margin: 0 auto;
		border: 1px solid black;
	}

	#writeZone {
		width: 20rem;
		margin: 0 auto;
	}

	.msg {
		list-style-type: none;
	}
</style>
