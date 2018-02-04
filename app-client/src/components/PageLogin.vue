<template>
	<div class="page-login">
		<div class="login-head">
			<div class="login-tip-pic">
				<img class="logo-pic" src="../images/login.png">
			</div>
			<div class="login-tip-text">
				<span>Log in to Free Talk</span>
			</div>
		</div>
		<div class="login-body">
			<div class="login-field">
				<div>
					<svg class="icon">
						<use xlink:href="../images/icons.svg#icon-truck"/>
					</svg>
					<input type="text" placeholder="请输入您的账号..." v-on:blur="validatorUser" v-model="username">
				</div>
				<div v-bind:class="[{ hide: isHide },tipClass]">账户名不存在</div>
			</div>
			<div class="login-field">
				<div>
					<svg class="icon">
						<use xlink:href="../images/icons.svg#icon-alarm"/>
					</svg>
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

	var namespace = '/validator'
	var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace)

	// socket.on('exist_user',function(msg){
	// 	let user_exist = msg['data']
	// 	if(!user_exist){
	// 		this.isHide = false
	// 	}
	// })
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
					self.$emit('change','chat-room')
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
				this.$emit('change','page-register')
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
		width: 50%;
		margin: 0 auto;
	}

	.login-tip-pic {
		text-align: center;
	}

	.login-tip-text {
		margin-top: 2rem;
		text-align: center;
	}

	.logo-pic {
		width: 6rem;
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

	.login-foot {
		display: flex;
		justify-content: center;
		margin: 1rem;
	}

	.hide,.pwdHide {
		display: none;
	}
	
	input {
		padding: 0.3rem;
	}

	.errorTip {
		font-size: 0.9rem;
    	color: red;
	}
</style>

