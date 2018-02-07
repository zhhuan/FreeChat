<template>
    <div id="page-register">
        <div id="register-body">
            <div id="register-content">
                <div class="register-field">
                    <span>username:</span><input v-model="reUser" type="text">
                </div>
                <div class="register-field">
                    <span>password:</span><input v-model="rePwd" type="password">
                </div>
                <div class="register-field">
                    <span>email:</span><input v-model="reEmail" type="email">
                </div>
            </div>
            <div id="register-tip">
                <span v-bind:class="[{ reHide: isHide },fieldClass]">帐户名已存在</span>
            </div>
        </div>
        <div id="register-foot">
            <button v-on:click="registerUser">确认</button>
        </div>
    </div>
    
</template>

<script>
    import io from 'socket.io-client'
    import {router} from '../util/util.js'
    
    var namespace = '/register'
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace)

    export default {
        data: function(){
            return {
                reUser: '',
                rePwd: '',
                reEmail: '',
                isHide: true,
                fieldClass: 'duplicate-tip'
            }
        },
        created: function() {
            let self = this
            socket.on('register_done',function(msg){
                let register_result = msg['data']
                if(register_result){
                    router.push({name:'login'})
                }else{
                    self.isHide = false
                }
            })
        },
        methods: {
            registerUser: function(){
                if(this.reUser && this.rePwd && this.reEmail){
                    socket.emit('register_user',{user:this.reUser,pwd:this.rePwd,email:this.reEmail})
                }else{
                    alert('please complete register msg')
                }
            }
        }
    }
</script>

<style>
    #page-register {
        width: 25rem;
        margin: 0 auto;
    }

    #register-body {
        display: flex;
    }

    #register-content {
        flex: 2;
    }

    .register-field {
        margin-top: 1rem;
        display: flex;
        justify-content: space-between;
        font-size: 0.9rem;
    }

    #register-tip {
        flex: 1;
        padding-top:1rem;
    }

    #register-foot {
        margin: 0 auto;
        width: 3rem;
        margin-top: 1rem;
    }

    .reHide {
        display: none;
    }

    .duplicate-tip {
        font-size: 0.9rem;
        color: red;
    }
</style>