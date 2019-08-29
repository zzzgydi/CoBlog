import Vue from 'vue'
import axios from 'axios'

function post(url, params) {
  return new Promise(function(resolve, reject) {
    axios
      .post(url, params || {})
      .then(res => {
        var data = res.data
        if (data.status !== 0 || data.data === undefined) {
          console.log('访问异常，状态码为' + data.status)
          reject(data.status)
        } else {
          resolve(data.data)
        }
      })
      .catch(err => {
        console.log('接口异常', err)
      })
  })
}

Vue.prototype.$post = post
