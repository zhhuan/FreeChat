import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue';
//import { router } from './util/util.js'

Vue.use(VueRouter);
Vue.config.debug = true;//开启错误提示
const app = new Vue(App);

// const app = new Vue({
//     router,
//     el:"#app",
//     // created: function() {
//     //     router.push({ path: '/' })
//     // }
// })
// const router = new VueRouter({
//     routes: [
//         {path: '/chatroom/:username',component: TalkField}
//     ]
// })

// const app = new Vue({
//     router
// }).$mount('#app')
