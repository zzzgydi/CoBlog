<template>
  <div class="login-cnt">
    <div class="slogan">
      <span>This is a</span>
      <br />
      <span class="login">Login</span> page
    </div>
    <el-input v-model="account" placeholder="请输入账号" @keypress.enter.native="clickLogin"></el-input>
    <el-input
      v-model="password"
      placeholder="请输入密码"
      show-password
      @keypress.enter.native="clickLogin"
    ></el-input>
    <div class="btn">
      <el-button type="primary" plain @click="clickLogin">登录</el-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      account: '',
      password: ''
    }
  },
  methods: {
    clickLogin() {
      if (this.account.length < 1 || this.password.length < 6) {
        this.$message.info('请输入有效的账号密码')
        return
      }
      this.$post('/api/login', {
        account: this.account,
        password: this.password
      })
        .then(res => {
          this.$store.commit('login')
          this.$store.commit('setAccount', res.account)
          this.$store.commit('setName', res.name)
          this.$message.success('登录成功')
          this.$router.replace('/center')
          // var arr = document.cookie.split(';')
          // var cookie = {}
          // for (let each of arr) {
          //   var tmp = each.split('=')
          //   cookie[tmp[0].trim()] = tmp[1]
          // }
          // localStorage.setItem('session', cookie.session)
        })
        .catch(() => {
          this.$message.error('账号或密码错误')
        })
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '../assets/css/default';

.login-cnt {
  // width: 40%;
  max-width: 350px;
  min-width: 200px;
  margin: 80px auto;
  padding: 40px 32px;
  background-color: #fefefe;
  border-radius(10px);
  box-shadow: 1px 2px 10px 0 rgba(0, 0, 0, 0.1);

  .el-input {
    margin-bottom: 20px;
  }

  .slogan {
    text-align: right;
    font-size: 2rem;
    font-weight: bold;
    text-transform: uppercase;
    color: default_black;
    margin-bottom: 30px;
    text-shadow: 2px 2px 2px rgba(16, 16, 16, 0.5);

    .login {
      color: theme_color;
    }
  }

  .btn {
    margin-top: 20px;
    text-align: center;

    .el-button {
      width: 200px;
    }
  }
}

@media screen and (max-width: mobile_width) {
  .login-cnt {
    background-color: transparent;
    box-shadow: none;
  }
}
</style>
