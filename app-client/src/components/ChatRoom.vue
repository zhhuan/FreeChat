<template>
	<div id="chatroom">
		<div id="roomName">test room</div>
		<div id="chatContent">
			<ul id="chatRecords">
				<talk-field v-for="conversation in conversations" v-bind="conversation"></talk-field>
			</ul>
		</div>
		<div id="writeZone">
			<img class="avator-default" src="/favicon/default.png">
			<input class="myTalk" v-model="sendMsg" type="text" placeholder="click here to type message">
			<button v-on:click="sendTalk">Send</button>
		</div>
	</div>
</template>
  
<script>
	import io from 'socket.io-client'
	import TalkField from './TalkField.vue'

	var namespace = '/chatroom'
	var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace)
	
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
					role: msg.role,
					word: msg.data
				})
			})
		},
		methods: {
			sendTalk: function() {
				socket.emit('send_msg',{data:this.sendMsg,role:this.$route.params.username})
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
		display: flex;
		width: 40rem;
		border: 1px solid black;
		margin: 0 auto;
	}

	.avator-default {
        width: 2.5rem;
		height: 100%;
        border-radius: 0.5rem;
		margin-left: 1.5rem;
        margin-right: 1.5rem;
    }

	.myTalk {
		width: 30rem;
    	border: none;
	}

	.msg {
		list-style-type: none;
	}
</style>
