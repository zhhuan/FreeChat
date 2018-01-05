<template>
    <div>
        <keep-alive>
            <component v-bind:is="currentView" v-on:change="changeView"></component>
        </keep-alive>
    </div>
</template>
<script>
	import PageLogin from './components/PageLogin.vue'
    import PageRegister from './components/PageRegister.vue'
    import ChatRoom from './components/ChatRoom.vue'

    export default {
        el:"#app",
        data: {
            currentView:'page-login'
        },
        methods: {
            changeView: function(msg){
                this.currentView = msg
            }
        },
        components: {
            'page-login': PageLogin,
            'page-register': PageRegister,
            'chat-room': ChatRoom
        }
    }
</script>