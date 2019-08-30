import axios from 'axios'

// axios.defaults.withCredentials = true

function post(url, params) {
  var that = this
  return new Promise(function(resolve, reject) {
    axios
      .post(url, params || {})
      .then(res => {
        var data = res.data
        if (data.status === 0) {
          // 访问成功
          resolve(data.data)
          return
        } else if (data.status === 100) {
          // 需要登录态但是没有登录
          console.log('登录态无效')
          if (that.$route.path.indexOf('/center') !== -1) {
            that.$router.replace('/login')
          }
        } else {
          console.log('访问异常，状态码为', data.status)
        }
        reject(data.status)
      })
      .catch(err => {
        console.log('接口异常', err)
      })
  })
}

export default {
  post
}
