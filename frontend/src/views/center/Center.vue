<template>
  <div class="center-cnt">
    <div
      class="router-box"
      v-for="path in paths"
      :key="path.url"
      @click="handleClick(path)"
      @mouseover="path._centerShow=true"
      @mouseout="path._centerShow=false"
    >
      <i :class="path.icon"></i>
      <span>&ensp;{{path.name}}</span>
      <div :hidden="!path._centerShow" style="float:right">
        <i class="el-icon-caret-right"></i>
      </div>
    </div>
    <div class="fix-box" v-for="fix in fixPaths" :key="fix"></div>
  </div>
</template>

<script>
import Config from '../../assets/js/config'

for (let i of Config.centerPaths) i._centerShow = false // 添加hover效果
for (let i of Config.mobilePaths) i._centerShow = false // 添加hover效果

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
        this.$router.push(path.url)
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

<style lang="stylus" scoped>
@import '../../assets/css/default';

.fix-box {
  height: 0px;
  width: 24%;
  padding: 0 30px;
}

.router-box {
  noselect();
  cursor: pointer;
  padding: 15px 30px;
  background-color: #fefefe;
  box-shadow: 0 1px 5px 0 rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
  line-height: 42px;
  font-size: 1.1rem;
  color: default_black;
  transition(0.12s);
  border-radius(6px);

  &:hover {
    font-size: 1.25rem;
    font-weight: bold;
    color: theme_color;
    box-shadow: 0 2px 12px 1px rgba(0, 0, 0, 0.1);
  }

  &:active {
    box-shadow: 0 2px 5px 1px rgba(0, 0, 0, 0.1) inset;
  }
}

@media screen and (min-width: mobile_width_1) {
  .center-cnt {
    width: 75%;
    margin: 50px auto;
    display: flex;
    display: -webkit-flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  .router-box {
    width: 24%;
  }
}

@media screen and (min-width: mobile_width) and (max-width: mobile_width_1) {
  .center-cnt {
    width: 75%;
    margin: 50px auto;
    display: flex;
    display: -webkit-flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  .router-box {
    width: 30%;
  }
}

@media screen and (max-width: mobile_width) {
  .center-cnt {
    // width: 90%;
    padding: 20px 8% 50px;
  }
}
</style>
