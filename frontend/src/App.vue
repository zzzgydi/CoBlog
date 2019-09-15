<template>
  <div id="app">
    <navigator></navigator>
    <div class="main-content" ref="content">
      <keep-alive :include="['editor', 'error', 'viewnote', 'bookcommon']">
        <router-view></router-view>
      </keep-alive>
    </div>
    <footer>&copy; 2019 note.segydi.cn</footer>
    <!-- <myfooter :domHeight="refHeight"></myfooter> -->
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
      // this.$store.commit('updateHeight', window.innerHeight)
    }
    this.$store.commit('updateWidth', window.innerWidth)
    // this.$store.commit('updateHeight', window.innerHeight)

    this.$post('/api/check')
      .then(res => {
        this.$store.commit('login')
        // this.$store.commit('setAccount', res.account)
        // this.$store.commit('setName', res.name)
        // this.$store.commit('setAvatar', res.avatar)
        // this.$store.commit('setBackimg', res.backimg)
        this.$store.commit('setUser', {
          account: res.account,
          name: res.name,
          avatar: res.avatar,
          backimg: res.backimg,
          alias: res.alias,
          flag: res.flag
        })
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
  background-color: #f6f6f6;
  // font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  position: fixed;
  top: 0;
  left: 0;
  // z-index: 100;
  width: 100%;
  /* 必须 */
  display: flex;
  /* 必须，规定元素的排列方向 */
  flex-direction: column;
  /* 必须占满屏 */
  height: 100%;
  /* 没有这个就不能滚动了 */
  overflow-y: auto;
  overflow-x: auto;
}

.main-content {
  width: 100%;
  margin-top: 20px;
  flex: 1; /* 占了百分百-flex:0的占位 */
}

footer {
  width: 100%;
  padding: 10px 0;
  text-align: center;
  flex: 0;
  color: #606266;
}

/* 滚动条样式 */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: rgb(239, 239, 239);
  border-radius: 2px;
}

::-webkit-scrollbar-thumb {
  background: #bfbfbf;
  border-radius: 6px;
}

::-webkit-scrollbar-thumb:hover {
  background: theme_color_a(0.5);
}

::-webkit-scrollbar-corner {
  background: #f6f6f6;
}
</style>
