<template>
  <div class="center-cnt">
    <div
      class="router-box"
      v-for="path in paths"
      :key="path.url"
      @click="handleClick(path)"
      @mouseover="path.show=true"
      @mouseout="path.show=false"
    >
      <i :class="path.icon"></i>
      <span>&ensp;{{path.name}}</span>
      <div :hidden="!path.show" style="float:right">
        <i class="el-icon-caret-right"></i>
      </div>
    </div>
    <div class="fix-box" v-for="fix in fixPaths" :key="fix"></div>
  </div>
</template>

<script>
import Config from '../../assets/js/config'

for (let i of Config.centerPaths) {
  i.show = false // 添加hover效果
}

export default {
  name: 'center',
  data() {
    return {
      paths: Config.centerPaths
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
  methods: {
    handleClick(path) {
      path.show = false
      if (path.url === 'logout') {
        this.$post('/api/logout').then(() => {
          this.$store.commit('logout')
          this.$router.replace('/')
        })
        return
      }
      this.$router.push(path.url)
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '../../assets/default';

.center-cnt {
  width: 75%;
  margin: 50px auto;
  display: flex;
  display: -webkit-flex;
  // align-content: flex-start;
  flex-wrap: wrap;
  justify-content: space-between;
}

.router-box {
  noselect();
  cursor: pointer;
  width: 24%;
  min-width: 100px;
  padding: 15px 30px;
  background-color: #fefefe;
  box-shadow: 0 1px 5px 0 rgba(0, 0, 0, 0.1);
  // flex-shrink: 0;
  margin-bottom: 30px;
  line-height: 42px;
  font-size: 1.1rem;
  color: default_black;
  transition(0.12s);

  &:hover {
    font-size: 1.25rem;
    font-weight: bold;
    color: theme_color;
    box-shadow: 0 2px 12px 1px rgba(0, 0, 0, 0.1);
  }
}

.fix-box {
  height: 0px;
  width: 24%;
  padding: 0 30px;
}
</style>
