<template>
    <div>
        <page-login></page-login>
    </div>
</template>
<script>
	import PageLogin from './components/PageLogin.vue'
    export default {
    	el:"#app",
        components: {
        	'page-login': PageLogin
        }
    }
</script>