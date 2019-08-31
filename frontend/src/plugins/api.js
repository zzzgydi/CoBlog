import axios from 'axios'

// axios.defaults.withCredentials = true

var waitMap = {}

// 获得一个对象
function getMapObj(wait) {
  return {
    mode: 'url', // 判断是key模式还是url模式
    wait: wait,
    previous: 0,
    cache: null,
    caches: null, // key模式
    times: null, // key模式 等价于 previous
    key: null // key模式 记录请求体的key值
  }
}

/**
 * 防抖缓存版post方法
 * 支持 对某个url的结果进行缓存，以及对某个url中的某个参数值不同进行缓存
 */
function post(url, params) {
  var that = this
  var key
  // 该接口已经设置了防抖
  return new Promise(function(resolve, reject) {
    let now = new Date()
    if (waitMap[url]) {
      // 直接从缓存获取
      if (waitMap[url].mode === 'url') {
        if (now - waitMap[url].previous < waitMap[url].wait) {
          resolve(waitMap[url].cache)
          return
        }
      } else {
        key = waitMap[url].key
        if (now - waitMap[url].times[params[key]] < waitMap[url].wait) {
          resolve(waitMap[url].caches[params[key]])
          return
        }
      }
    }

    axios
      .post(url, params || {})
      .then(res => {
        var data = res.data
        if (data.status === 0) {
          resolve(data.data) // 访问成功
          // 设置节流器
          if (waitMap[url]) {
            if (waitMap[url].mode === 'url') {
              waitMap[url].previous = new Date()
              waitMap[url].cache = data.data
            } else {
              key = waitMap[url].key
              waitMap[url].times[params[key]] = new Date()
              waitMap[url].caches[params[key]] = data.data
            }
          }
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

// 添加防抖的url
function setThrottle(url, wait, params) {
  waitMap[url] = getMapObj(wait)
  if (params) {
    waitMap[url].mode = 'key'
    waitMap[url].times = {}
    waitMap[url].caches = {}
    waitMap[url].key = params
  }
}

export default {
  post,
  setThrottle
}
