import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import axios from 'axios'
// import mavonEditor from 'mavon-editor'
// import 'mavon-editor/dist/css/index.css'
import './plugins/element.js'
import './plugins/api.js'

Vue.config.productionTip = false
// Vue.prototype.$axios = axios
// Vue.use(mavonEditor)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
