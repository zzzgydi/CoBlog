<template>
  <div id="app">
    <navigator></navigator>
    <div class="main-content">
      <keep-alive :include="['editor', 'error', 'viewnote', 'bookcommon']">
        <router-view></router-view>
      </keep-alive>
    </div>
  </div>
</template>

<script>
import Navigator from '@/components/Navigator.vue'
export default {
  name: 'app',
  components: {
    navigator: Navigator
  },
  methods: {
    watchLoginPath() {
      // 对页面进行登录确认
      if (this.$route.path.indexOf('/center') !== -1) {
        this.$router.replace('/login')
      }
    }
  },
  beforeMount() {
    // 设置监听窗口变化
    window.onresize = () => {
      this.$store.commit('updateWidth', window.innerWidth)
    }
    this.$store.commit('updateWidth', window.innerWidth)

    this.$post('/api/check')
      .then(res => {
        this.$store.commit('login')
        this.$store.commit('setAccount', res.account)
        this.$store.commit('setName', res.name)
        this.$store.commit('setAvatar', res.avatar)
        this.$store.commit('setBackimg', res.backimg)
      })
      .catch(() => {
        this.$store.commit('logout') // 登录态无效
        // this.watchLoginPath() // 对当前页面进行登录确认
        // this.$router.replace('/login')
      })
    this.$router.beforeEach((to, from, next) => {
      if (!this.$store.state.ifLogin && to.path.indexOf('/center') !== -1) {
        next({
          replace: true,
          path: '/404'
        })
      }
      next()
    })
  }
}
</script>

<style lang="stylus">
@import './assets/css/default';

* {
  padding: 0;
  margin: 0;
}

body {
  overflow-y: scroll;
  background-color: #f6f6f6;
  // font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.main-content {
  margin-top: 20px;
}
</style>
