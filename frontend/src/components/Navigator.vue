<template>
  <div class="navigator">
    <el-row>
      <el-col :span="6">
        <div class="topic">{{navList.topic}}</div>
      </el-col>

      <el-col :span="18">
        <div class="beforeLogin" v-if="!ifLogin">
          <el-menu
            :default-active="this.$route.path"
            router
            class="menu"
            mode="horizontal"
            @select="handleSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b"
          >
            <el-menu-item :index="navList.addNote.url">{{navList.addNote.name}}</el-menu-item>
            <el-menu-item :index="navList.drafts.url">{{navList.drafts.name}}</el-menu-item>
            <el-submenu :index="navList.personalCenter.url">
              <template slot="title">{{navList.personalCenter.name}}</template>
              <el-menu-item index="3-1">选项1</el-menu-item>
              <el-menu-item index="3-2">选项2</el-menu-item>
              <el-menu-item index="3-3">选项3</el-menu-item>
            </el-submenu>
          </el-menu>
        </div>
        <div class="afterLogin" v-else>
          <el-menu
            :default-active="this.$route.path"
            router
            class="menu"
            mode="horizontal"
            @select="handleSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b"
          >
            <el-menu-item :index="navList.register.url">{{navList.register.name}}</el-menu-item>
            <el-menu-item :index="navList.login.url">{{navList.login.name}}</el-menu-item>
          </el-menu>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'Navigator',
  computed: {
    ifLogin() {
      return this.$store.state.ifLogin
    }
  },
  data() {
    return {
      navList: {
        topic: 'CO-NOTE',
        addNote: {
          url: '/edit',
          name: '添加笔记'
        },
        drafts: {
          url: '/drafts',
          name: '草稿箱'
        },
        personalCenter: {
          url: '/personal',
          name: '个人中心'
        },
        register: {
          url: '/register',
          name: '注册'
        },
        login: {
          url: '/login',
          name: '登录'
        }
      }
    }
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath)
      console.log(this.$route)
      console.log(this.$route.path)
      // this.$router.push({name:})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="stylus">
.navigator {
  background-color: rgb(84, 92, 100);
  height: 60px;
}

.topic {
  border-radius: 4px;
  height: 60px;
  background: #99a9bf;
  text-align: center;
  line-height: 60px;
  font-size: 24px;
}

.beforeLogin, .afterLogin {
  margin-left: 50%;
  display: flex;
  justify-content: space-around;
}

.el-col {
  border-radius: 4px;
}
</style>
