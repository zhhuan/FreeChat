import VueRouter from 'vue-router'

import PageLogin from '../components/PageLogin.vue'
import PageRegister from '../components/PageRegister.vue'
import ChatRoom from '../components/ChatRoom.vue'

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', name: 'login', component: PageLogin},
        { path: '/register', name: 'register', component: PageRegister},
        { path: '/chatroom/:username', name: 'chatroom', component: ChatRoom}
    ]
})

export { router }