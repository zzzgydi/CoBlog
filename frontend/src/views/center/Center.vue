<template>
  <div class="center-cnt">
    <div class="welcome-cnt">
      Hello
      <span>{{userName}}</span>
      !!
    </div>
    <div class="router-cnt">
      <div class="router-box" v-for="path in paths" :key="path.url" @click="handleClick(path)">
        <i :class="path.icon"></i>
        <span>&ensp;{{path.name}}</span>
        <div class="hover-arrow">
          <i class="el-icon-caret-right"></i>
        </div>
      </div>
      <div class="fix-box" v-for="fix in fixPaths" :key="fix"></div>
    </div>
  </div>
</template>

<script>
import Config from '../../assets/js/config'

export default {
  name: 'center',
  data() {
    return {
      paths: []
    }
  },
  computed: {
    fixPaths() {
      // 用于flex布局的space-between属性填充多个div
      var len = this.paths.length
      var c = 3 * Math.ceil(len / 3) - len
      var a = []
      for (let i = 0; i < c; ++i) {
        a.push('--' + i)
      }
      return a
    },
    userName() {
      return this.$store.state.name || '未命名'
    }
  },
  watch: {
    '$store.state.ssize': function(newVal) {
      if (this.$store.state.ssize === 0) {
        this.paths = Config.mobilePaths // 移动端的中心页采用和导航栏的一样
      } else {
        this.paths = Config.centerPaths
      }
    }
  },
  methods: {
    handleClick(path) {
      path._centerShow = false
      if (path.url === 'logout') {
        this.$confirm('是否确认退出登录', '提示')
          .then(() => {
            this.$post('/api/logout').then(() => {
              this.$store.commit('logout')
              this.$message.success('登出成功')
              if (this.$route.path !== '/') this.$router.replace('/')
            })
          })
          .catch(e => e)
      } else if (this.$route.path !== path.url) {
        setTimeout(() => {
          this.$router.push(path.url)
        }, 200)
      }
    }
  },
  beforeMount() {
    if (this.$store.state.ssize === 0) {
      this.paths = Config.mobilePaths // 移动端的中心页采用和导航栏的一样
    } else {
      this.paths = Config.centerPaths
    }
  }
}
</script>

<style lang="stylus" scoped src="../../assets/css/view.styl"></style>
