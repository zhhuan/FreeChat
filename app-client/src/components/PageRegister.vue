<template>
    <div id="page-register">
        <div id="register-body">
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
        <div id="register-foot">
            <button v-on:click="registerUser">确认</button>
        </div>
    </div>
    
</template>

<script>
    export default {
        data: function(){
            return {
                reUser: '',
                rePwd: '',
                reEmail: ''
            }
        },
        methods: {
            registerUser: function(){
                if(this.reUser && this.rePwd && this.reEmail){
                    this.$emit('change','page-login')
                }else{
                    alert('please complete register msg')
                }
            }
        }
    }
</script>

<style>
    #page-register {
        width: 20rem;
        margin: 0 auto;
    }

    .register-field {
        margin-top: 1rem;
    }

    #register-foot {
        padding-top: 1rem;
        padding-left: 2rem;
    }
</style>