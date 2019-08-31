import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import api from './plugins/api.js'
// import mavonEditor from 'mavon-editor'
// import 'mavon-editor/dist/css/index.css'
import './plugins/element.js'

// Vue.use(mavonEditor)
Vue.config.productionTip = false
Vue.prototype.$post = api.post

// 对接口设置节流
api.setThrottle('/api/getnotes', 5000)
api.setThrottle('/api/usernotes', 5000, 'state')

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
