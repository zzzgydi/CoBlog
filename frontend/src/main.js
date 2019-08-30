import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import api from './plugins/api.js'
// import axios from 'axios'
// import mavonEditor from 'mavon-editor'
// import 'mavon-editor/dist/css/index.css'
import './plugins/element.js'

// Vue.prototype.$axios = axios
// Vue.use(mavonEditor)
Vue.config.productionTip = false
Vue.prototype.$post = api.post

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
