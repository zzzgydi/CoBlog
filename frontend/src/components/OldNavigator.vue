<template>
  <div class="navigator">
    <div class="logo-box" @click="handleClick('/')">
      <img src="../assets/img/logo.png" class="logo-img" />
      <!-- <i class="el-icon-cloudy"></i> -->
      <span>CoNote</span>
    </div>
    <div class="options-box">
      <div
        v-for="item in navList"
        :class="item.url===$route.path?'option-active':'option'"
        :key="item.url"
        @click="handleClick(item.url)"
      >{{item.name}}</div>
    </div>
  </div>
</template>

<script>
import Config from '../assets/js/config'

export default {
  name: 'Navigator',
  computed: {
    ifLogin() {
      return this.$store.state.ifLogin
    },
    navList() {
      return this.$store.state.ifLogin
        ? Config.navListLogin
        : Config.navListNotLogin
    }
  },
  data() {
    return {}
  },
  methods: {
    handleClick(url) {
      if (this.$route.path !== url) {
        this.$router.push(url)
      }
    }
  }
}
</script>

<style scoped lang="stylus">
@import '../assets/default';

nav_height = 60px;

.navigator {
  background-color: default_white;
  height: nav_height;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
}

.logo-box {
  // width: 10%;
  noselect();
  cursor: pointer;
  line-height: nav_height;
  color: default_black;
  font-size: 1.5rem;
  float: left;
  margin-left: 2%;
  display: flex;
  display: -webkit-flex;
  align-items: center;

  .logo-img {
    width: 36px;
    margin-right: 6px;
  }
}

option-style() {
  cursor: pointer;
  width: 5.8rem;
  text-align: center;
  transition(0.1s);
}

.options-box {
  noselect();
  float: right;
  display: flex;
  display: -webkit-flex;
  line-height: nav_height;
  margin-right: 2%;

  .option {
    option-style();
    color: default_black;
  }

  .option:hover {
    font-size: 1.25rem;
  }

  .option-active {
    option-style();
    font-size: 1.25rem;
    font-weight: 600;
    color: theme_color;
  }
}
</style>
