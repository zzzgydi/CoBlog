<template>
  <div id="app">
    <navigator></navigator>
    <div class="main-content">
      <keep-alive :include="['home', 'editor', 'error', 'viewnote']">
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
  beforeMount() {
    this.$router.beforeEach((to, from, next) => {
      if (!this.$store.state.ifLogin) {
        // 对页面进行登录确认
        if (to.path.indexOf('/center') !== -1) {
          next({
            replace: true,
            path: '/404'
          })
        }
      }
      next()
    })
  }
}
</script>

<style>
* {
  padding: 0;
  margin: 0;
}

body {
  overflow-y: scroll;
  background-color: #f0f3fa55;
  /* font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50; */
}

.main-content {
  margin-top: 20px;
}
</style>
