import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import api from './plugins/api.js'
// import mavonEditor from 'mavon-editor'
// import 'mavon-editor/dist/css/index.css'
import './plugins/element.js'

import { MessageBox, Message } from 'element-ui'
import { Dialog } from 'vant'

// Vue.use(mavonEditor)
Vue.config.productionTip = false
Vue.prototype.$post = api.post

// 对接口设置节流
api.setThrottle('/api/getnotes', 5000)
api.setThrottle('/api/usernotes', 5000, 'state')

// element-ui的MessageBox在移动端样式不好
function newConfirm(message, title, options) {
  var that = this
  return new Promise(function(resolve, reject) {
    if (that.$store.state.ssize === 0) {
      // 移动端
      Dialog.confirm({
        title: title,
        message: message
      })
        .then(resolve)
        .catch(reject)
    } else {
      // PC端
      MessageBox.confirm(message, title, options)
        .then(resolve)
        .catch(reject)
    }
  })
}

// 将element-ui的Message的时间持续时间统一修改为1000ms
var newMessage = Message
;['success', 'warning', 'info', 'error'].forEach(function(type) {
  newMessage[type] = function(options) {
    var duration
    if (vm.$store.state.ssize === 0) duration = 800
    else duration = 1500
    if (typeof options === 'string') {
      options = {
        message: options,
        duration: duration
      }
    }
    options.type = type
    return Message(options)
  }
})

var vm = new Vue({
  router,
  store,
  render: h => h(App)
})

Vue.prototype.$message = newMessage
Vue.prototype.$confirm = newConfirm.bind(vm)
vm.$mount('#app')
