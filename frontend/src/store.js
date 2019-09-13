import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
const defaultAvatar =
  'https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png' // element里拿的

export default new Vuex.Store({
  state: {
    ifLogin: false,
    account: '未登录',
    name: '未登录',
    avatar: defaultAvatar, // 头像地址
    backimg: '', // 背景图地址
    screenWidth: window.innerWidth, // 监控宽度
    screenSize: 'large',
    ssize: 0
  },
  getters: {
    ifLogin: state => state.ifLogin
  },
  mutations: {
    login(state) {
      if (state.ifLogin) return
      state.ifLogin = true
    },
    logout(state) {
      if (!state.ifLogin) return
      state.ifLogin = false
      state.account = '未登录'
      state.name = '未登录'
    },
    setAccount(state, account) {
      state.account = account
    },
    setName(state, name) {
      state.name = name || '用户'
    },
    setAvatar(state, avatar) {
      state.avatar = avatar || defaultAvatar
    },
    setBackimg(state, backimg) {
      state.backimg = backimg
    },
    updateWidth(state, width) {
      // 传入屏幕宽度，将屏幕分三个等级
      state.screenWidth = width
      if (width < 430) {
        state.screenSize = 'small'
        state.ssize = 0
      } else if (width < 770) {
        state.screenSize = 'medium'
        state.ssize = 1
      } else {
        state.screenSize = 'large'
        state.ssize = 2
      }
    }
  },
  actions: {}
})
