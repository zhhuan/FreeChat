<template>
    <router-view></router-view>
</template>

<script>
    import { router } from './util/util.js'
    export default {
        router,
        el:"#app",
        created: function() {
            router.push({ path: '/' })
        }
    }
</script>