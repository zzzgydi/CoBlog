<template>
  <div class="navigator">
    <div class="logo-box" @click="handleClick('/')">
      <img src="../assets/img/logo.png" class="logo-img" />
      <div v-show="!(judgeMenu && showPageTitle)">
        <span>Co</span>
        <span class="note">Note</span>
      </div>
      <div class="page-title" v-show="judgeMenu">{{showPageTitle}}</div>
    </div>

    <div class="mobile-menu" v-if="judgeMenu && ifLogin">
      <div class="menu-icon" @click="clickMobileMenu">
        <i class="el-icon-menu"></i>
      </div>
      <van-popup v-model="showPopup" :style="{ height: '100%', width: '60%' }" position="right">
        <div class="popup-cnt">
          <div class="pop-logo">
            <i class="el-icon-cloudy note"></i>
            <span>&ensp;Co</span>
            <span class="note">Note</span>
          </div>
          <div
            v-for="item in popupList"
            :class="item.url===$route.path?'pop-active':'pop-opt'"
            :key="item.url"
            @click="handleClick(item.url)"
          >
            <i :class="item.icon"></i>
            {{item.name}}
          </div>
        </div>
      </van-popup>
    </div>

    <div class="options-box" v-else>
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
var navObj = Config.navObj

export default {
  name: 'Navigator',
  computed: {
    ifLogin() {
      return this.$store.state.ifLogin
    },
    navList() {
      if (this.$store.state.ifLogin) {
        switch (this.$store.state.ssize) {
          case 1: //  中等
            return [navObj.home, navObj.books, navObj.center]
          case 2: // large
            return [navObj.home, navObj.books, navObj.private, navObj.center]
        }
        return []
      } else {
        return [navObj.home, navObj.login]
      }
    },
    popupList() {
      return Config.mobilePaths
    },
    judgeMenu() {
      return this.$store.state.ssize === 0 // 屏幕等级为小
    },
    showPageTitle() {
      return Config.pageTitleMap[this.$route.path] || ''
    }
  },
  data() {
    return {
      showPopup: false
    }
  },
  methods: {
    handleClick(url) {
      // 在这个页面点击了登出，就一定是pop菜单触发的
      if (url === 'logout') {
        this.showPopup = false
        this.$confirm('是否确认退出登录', '提示')
          .then(() => {
            this.$post('/api/logout').then(() => {
              this.$store.commit('logout')
              this.$message.success('登出成功')
              if (this.$route.path !== url) this.$router.replace('/')
            })
          })
          .catch(e => e)
      } else if (this.$route.path !== url) {
        this.$router.push(url)
        this.showPopup = false
      }
    },
    clickMobileMenu() {
      this.showPopup = true
    }
  }
}
</script>

<style scoped lang="stylus">
@import '../assets/css/default';

nav_height = 60px;

.navigator {
  background-color: default_white;
  height: nav_height;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.12);
  display: flex;
  display: -webkit-flex;
  justify-content: space-between;
  padding-left: 2%;
  padding-right: 2%;
}

.logo-box {
  // width: 10%;
  noselect();
  cursor: pointer;
  line-height: nav_height;
  color: default_black;
  display: flex;
  display: -webkit-flex;
  align-items: center;
  text-shadow: 1px 2px 2px rgba(0, 0, 0, 0.25);
  font-weight: 600;
  text-transform: uppercase;

  .note {
    color: theme_color;
  }
}

.page-title {
  color: theme_color;
  text-shadow: none;
}

@media screen and (max-width: mobile_width) {
  .logo-box {
    font-size: 1.2rem;
  }

  .logo-img {
    width: 28px;
    margin-right: 4px;
  }

  .navigator {
    padding-left: 15px;
    padding-right: 15px;
  }
}

@media screen and (min-width: mobile_width) {
  .logo-box {
    font-size: 1.5rem;
  }

  .logo-img {
    width: 36px;
    margin-right: 6px;
  }

  .navigator {
    padding-left: 2%;
    padding-right: 2%;
  }
}

option-style() {
  cursor: pointer;
  width: 5.8rem;
  text-align: center;
  transition(0.06s);
}

.options-box {
  noselect();
  float: right;
  display: flex;
  display: -webkit-flex;
  line-height: nav_height;

  .option {
    option-style();
    color: default_black;
  }

  .option:hover {
    color: theme_color;
    font-size: 1.25rem;
    font-weight: bold;
  }

  .option-active {
    option-style();
    font-size: 1.25rem;
    font-weight: bold;
    color: theme_color;
  }
}

.mobile-menu {
  .menu-icon {
    cursor: pointer;
    font-size: 2rem;
    line-height: nav_height;
    color: theme_color;
  }

  .pop-logo {
    color: default_black;
    font-size: 1.25rem;
    font-weight: 600;
    text-transform: uppercase;
    text-shadow: 1px 2px 2px rgba(0, 0, 0, 0.2);
    text-align: center;
    padding: 40px 0;

    .note {
      color: theme_color;
    }
  }

  .popup-cnt {
    height: 100%;
    overflow-x: hidden;
    background-color: default_white;

    popOption() {
      cursor: pointer;
      font-size: 1rem;
      color: default_color;
      padding: 15px 50px 15px 30px;
      border-top: 1px solid #eee;
      letter-spacing: 1.5px;
    }

    .pop-opt {
      popOption();

      &:last-child {
        border-bottom: 1px solid #eee;
      }
    }

    .pop-active {
      popOption();
      color: theme_color;
      font-weight: bold;
    }
  }
}
</style>
