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
				<svg class="icon">
					<use xlink:href="../images/icons.svg#icon-truck"/>
				</svg>
				<input type="text" name="username" placeholder="请输入您的账号...">
			</div>
			<div class="login-field">
				<svg class="icon">
					<use xlink:href="../images/icons.svg#icon-alarm"/>
				</svg>
				<input type="password" name="password" placeholder="请输入您的密码...">
			</div>
		</div>
		<div class="login-foot">
			<button id="login-btn" v-on:click="loginChatroom">登陆</button>
			<button id="register-btn" v-on:click="jumpRegister">注册</button>
		</div>
	</div>
</template>

<script>
	export default {
		data: function () {
			return 
		},
		methods: {
			loginChatroom: function () {
				this.$emit('change','chat-room')
			},
			jumpRegister: function () {
				this.$emit('change','page-register')
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
	}

	.login-foot {
		display: flex;
		justify-content: center;
		margin: 1rem;
	}

	input {
		padding: 0.3rem;
	}
</style>

