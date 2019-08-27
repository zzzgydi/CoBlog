import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    ifLogin: true
  },
  getters: {
    ifLogin: state => state.ifLogin
  },
  mutations: {
    change(state, ifLogin) {
      state.ifLogin = ifLogin;
    }
  },
  actions: {}
});
