<template>
  <div class="login-cnt">
    <div v-show="showLogin">
      <div class="slogan">
        <span>This is a</span>
        <br />
        <span class="login">Login</span> page
      </div>
      <el-input
        style="margin-bottom:20px;"
        v-model="account"
        placeholder="请输入账号"
        @keypress.enter.native="clickLogin"
      ></el-input>
      <el-input
        v-model="password"
        placeholder="请输入密码"
        show-password
        @keypress.enter.native="clickLogin"
      ></el-input>
      <div class="a-link">
        <span @click="switchToReg">点击注册</span>
      </div>
      <div class="btn">
        <el-button type="primary" plain @click="clickLogin">登录</el-button>
      </div>
    </div>

    <div v-show="!showLogin">
      <div class="slogan">
        <span>This is a</span>
        <br />
        <span class="login">Register</span> page
      </div>
      <el-input
        style="margin-bottom:20px;"
        v-model="regAccount"
        placeholder="请输入账号"
        :maxlength="32"
        @input="handleAccount"
      ></el-input>
      <el-input
        style="margin-bottom:20px;"
        v-model="regPwd"
        placeholder="请输入密码"
        show-password
        :maxlength="18"
        @input="handlePwd"
      ></el-input>
      <el-input
        style="margin-bottom:20px;"
        v-model="regPwd2"
        placeholder="请确认密码"
        show-password
        :maxlength="18"
        @input="handlePwd"
      ></el-input>
      <div class="rand-img-line">
        <el-input
          style="width: 60%"
          v-model="regCode"
          placeholder="请输入验证码"
          @keyup.enter.native="clickRegister"
        ></el-input>
        <div class="img-cnt">
          <img :src="randimg" alt="验证码" />
        </div>
      </div>
      <div class="a-link reg-link">
        <span @click="returnToLogin">返回登录</span>
        <span @click="clickChangeImg">{{seconds === 0 ? '点击切换' : ('等待 '+seconds+'s')}}</span>
      </div>
      <div class="btn">
        <el-button type="primary" plain @click="clickRegister">注册</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import Tool from '../assets/js/tool'

export default {
  data() {
    return {
      showLogin: true, // 展示登录页
      account: '',
      password: '',
      regAccount: '', // 注册
      regPwd: '',
      regPwd2: '',
      regCode: '',
      randimg: '',
      beentry: 0, // 已经切换的次数
      seconds: 0
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
        password: Tool.encrypt(this.password)
      })
        .then(res => {
          this.$store.commit('login')
          this.$store.commit('setAccount', res.account)
          this.$store.commit('setName', res.name)
          this.$store.commit('setAvatar', res.avatar)
          this.$store.commit('setBackimg', res.backimg)
          this.$message.success('登录成功')
          this.$router.replace('/center')
        })
        .catch(() => {
          this.$message.error('账号或密码错误')
        })
    },
    clickRegister() {
      if (this.regAccount.length < 4) {
        return this.$message.info('请输入4位以上的账号名')
      }
      if (this.regPwd.length < 6) {
        return this.$message.info('密码至少6位')
      }
      if (this.regPwd !== this.regPwd2) {
        return this.$message.info('两次密码不匹配')
      }
      if (this.regCode.length !== 4) {
        return this.$message.info('验证码有误')
      }

      this.$post('/api/register', {
        account: this.regAccount,
        password: Tool.encrypt(this.regPwd),
        code: this.regCode
      })
        .then(res => {
          this.$message.success('注册成功')
          this.account = this.regAccount
          this.password = this.regPwd
          this.regAccount = ''
          this.regPwd = ''
          this.regPwd2 = ''
          this.regCode = ''
          this.showLogin = true // 跳转到登录页
        })
        .catch(err => {
          var msg = '未知错误'
          switch (err) {
            case 103:
              msg = '用户名已存在'
              break
            case 106:
              msg = '账户名格式有误'
              break
            case 107:
              msg = '密码格式有误'
              break
            case 108:
              msg = '验证码有误'
              this.getRandImg()
              this.regCode = ''
          }
          this.$message.error(msg)
        })
    },
    clickChangeImg() {
      // 第一次点击
      if (this.beentry < 8) {
        this.beentry += 1
        return this.getRandImg()
      }
      // 第二次之后点击
      if (!this._clock) {
        this.getRandImg()
        this.seconds = 10
        this._clock = setInterval(() => {
          this.seconds -= 1
          if (this.seconds <= 0) {
            clearInterval(this._clock)
            this._clock = null
          }
        }, 1000)
      }
    },
    switchToReg() {
      this.showLogin = false
      this.getRandImg()
    },
    returnToLogin() {
      this.showLogin = true
    },
    getRandImg() {
      this.$post('/api/randimg').then(res => {
        this.randimg = res.img
      })
    },
    handleAccount(val) {
      if (/[^0-9a-zA-Z]/.test(val)) {
        this.regAccount = this.regAccount.replace(/[^0-9a-zA-Z]/g, '')
        if (!this._regacc_tip) {
          this.$message.info('账号应为字母或数字的组合')
          this._regacc_tip = true
        }
      }
    },
    handlePwd(val) {
      if (/[^a-zA-Z0-9-*/+.~!@#$%^&*()_]/.test(val)) {
        this.regPwd = this.regPwd.replace(/\s/g, '')
        this.regPwd2 = this.regPwd2.replace(/\s/g, '')
        if (!this._regpwd_tip) {
          this.$message.info('密码应为字母,数字和标点符号的组合')
          this._regpwd_tip = true
        }
      }
    }
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/view.styl"></style>
