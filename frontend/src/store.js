import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    ifLogin: false
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
    }
  },
  actions: {}
})
