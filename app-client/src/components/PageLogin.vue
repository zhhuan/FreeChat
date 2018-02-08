<template>
	<div class="page-login">
		<div class="login-head">
			<div class="login-tip-pic">
				<h2 class="login-logo">Login Logo</h2>
			</div>
			<div class="login-tip-text">
				<span>Log in</span>
			</div>
		</div>
		<div class="login-body">
			<div class="login-field">
				<div>
					<h3 class="login-label">Username</h3>
					<input type="text" placeholder="请输入您的账号..." v-on:blur="validatorUser" v-model="username">
				</div>
				<div v-bind:class="[{ hide: isHide },tipClass]">账户名不存在</div>
			</div>
			<div class="login-field">
				<div>
					<h3 class="login-label">Password</h3>
					<input type="password"  placeholder="请输入您的密码..." v-model="password">
				</div>
				<div v-bind:class="[{ pwdHide: pwdHide },tipClass]">密码输入错误</div>
			</div>
		</div>
		<div class="login-foot">
			<button id="login-btn" v-on:click="loginChatroom">登陆</button>
			<button id="register-btn" v-on:click="jumpRegister">注册</button>
		</div>
	</div>
</template>

<script>
	import io from 'socket.io-client'
	import { router } from '../util/util.js'

	var namespace = '/validator'
	var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace)

	export default {
		data: function () {
			return {
				username: '',
				password: '',
				isHide: true,
				pwdHide: true,
				tipClass: 'errorTip'
			}
		},
		created: function() {
			let self = this
			socket.on('login_done', function(msg){
				let check_done = msg['data']
				if(check_done){
					router.push({ name:'chatroom', params:{ username:msg['username'] }})
					// self.$emit('change','chat-room')
				}else{
					self.pwdHide = false
				}
			})
			socket.on('exist_user',function(msg){
				let user_exist = msg['data']
				if(!user_exist){
					self.isHide = false
				}else{
					self.isHide = true
				}
			})
		},
		methods: {
			loginChatroom: function () {
				socket.emit('login_room', {username:this.username,password:this.password})
			},
			jumpRegister: function () {
				router.push({ name:'register' })
				// this.$emit('change','page-register')
			},
			validatorUser: function() {
				socket.emit('validator_user',{data:this.username})
			}
		}
	}
</script>

<style>
	.icon {
		display: inline-block;
		width: 1em;
		height: 1em;
		fill: currentColor;
	}

	.page-login {
		height: 100%;
		margin: 0 auto;
		background: #252527 url(/images/fillfeature.png);
	}

	.login-head {
		display: flex;
		justify-content: center;
	}

	.login-logo {
		width: 3rem;
		height: 3rem;
		font: 0/0 a;
		background: url(/images/login.png) no-repeat;
    	background-size: 3rem 3rem; 
    	opacity: 0.5;
	}

	.login-tip-text {
		padding-right: 8rem;
		font-size: 2.5rem;
		color: white;
	}

	.login-body {
		margin: 0 12rem;
	}

	.login-field {
		display: flex;
		margin-top: 1rem;
		justify-content: center;
		flex-direction: column;
		align-items: center;
	}

	.login-label {
		color: #999;
	}

	.login-foot {
		display: flex;
		justify-content: center;
		margin: 1rem;
	}

	.hide,.pwdHide {
		display: none;
	}
	
	input {
		padding: 1rem;
		border-radius: 0.5rem;
		font-size: 1.3rem;
	}

	button {
		padding: 10px 16px;
		border-radius: 3px;
		border: 3px solid transparent;
		outline: 0;
		font-size: 1rem;
		line-height: 1.2;
		color: white;
		background: #47cf73;
		cursor: pointer;
	}

	.login-foot button{
		margin: 0 10px 0 0;
	}
	.errorTip {
		width: 6rem;
		font-size: 0.9rem;
    	color: red;
	}
</style>

