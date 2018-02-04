<template>
	<div id="chatroom">
		<div id="roomName">test room</div>
		<div id="chatContent">
			<ul id="chatRecords">
				<talk-field v-for="conversation in conversations" v-bind="conversation"></talk-field>
			</ul>
		</div>
		<div id="writeZone">
			<input v-model="sendMsg" type="text" name="myTalk">
			<button v-on:click="sendTalk">Send</button>
		</div>
	</div>
</template>
  
<script>
	import io from 'socket.io-client'
	import TalkField from './TalkField.vue'

	var namespace = '/chatroom'
	var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace)
	
	// socket.on('pub_msg',function(msg){
	// 	var chatRecords = document.getElementById('chatRecords')
	// 	var wordHtml = '<li class="msg">'+msg.data+'</li>'
	// 	chatRecords.insertAdjacentHTML('beforeEnd',wordHtml)
	// })
	
	export default {
		data: function(){
			return {
				sendMsg:'',
				conversations:[]
			}
		},
		created:function(){
			let self = this
			socket.on('pub_msg', function(msg) {
				self.conversations.push({
					role: 'zhongh',
					word: msg.data
				})
			})
		},
		methods: {
			sendTalk: function() {
				socket.emit('send_msg',{data:this.sendMsg})
			}
		},
		components: {
			'talk-field':TalkField
		}
	}
</script>

<style>
	#roomName {
		text-align: center;
	}

	#chatContent {
		width: 40rem;
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
