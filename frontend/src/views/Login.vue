<template>
  <div style="width: 300px; margin: 20px auto;">
    <el-input v-model="account"></el-input>
    <el-input v-model="password"></el-input>
    <el-button @click="clickLogin">登录</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      account: 'gydi',
      password: '123456'
    }
  },
  methods: {
    clickLogin() {
      this.$post('/api/login', {
        account: this.account,
        password: this.password
      })
        .then(res => {
          this.$store.commit('login', true)
          this.$router.replace('/center')

          // var arr = document.cookie.split(';')
          // var cookie = {}
          // for (let each of arr) {
          //   var tmp = each.split('=')
          //   cookie[tmp[0].trim()] = tmp[1]
          // }
          // localStorage.setItem('session', cookie.session)
        })
        .catch(err => {
          this.$message.error('账号或密码错误')
        })
    }
  }
}
</script>

<style lang="stylus" scoped></style>