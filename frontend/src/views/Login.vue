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
        })
        .catch(() => {
          this.$message.error('账号或密码错误')
        })
    }
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/view.styl"></style>
