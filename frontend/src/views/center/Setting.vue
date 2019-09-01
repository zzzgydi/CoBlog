<template>
  <div>
    <div :class="assertSmall?'setting-box':'setting-box'">
      <div class="tips-box">
        <div class="setting-line">
          <div class="setting-label">
            <span class="label-1">这是</span>
            <span class="label-2">账号</span>
          </div>
          <div>
            <div class="setting-value">{{account}}</div>
            <div class="tips">登录用的 不能变的</div>
          </div>
        </div>
      </div>
      <div class="tips-box">
        <div class="setting-line">
          <div class="setting-label">
            <span class="label-1">这是</span>
            <span class="label-2">用户名</span>
          </div>
          <div>
            <div class="setting-value">{{name}}</div>
            <div class="tips">别人叫的 给你看的</div>
          </div>
        </div>
      </div>

      <div class="setting-revise name-input">
        <div class="setting-line-no">
          <div class="setting-label">
            <span class="label-1">修改</span>
            <span class="label-2">用户名</span>
          </div>
          <div class="tips">有字就行...</div>
        </div>
        <div class="setting-line">
          <el-input v-model="newName" placeholder="请输入新的用户名" @keypress.enter.native="clickSetName"></el-input>&emsp;
          <el-button type="primary" plain @click="clickSetName">修改</el-button>
        </div>
      </div>
      <div class="setting-revise pwd-input">
        <div class="setting-line-no">
          <div class="setting-label">
            <span class="label-1">修改</span>
            <span class="label-2">密码</span>
          </div>
          <div class="tips">密码至少6位 !!!</div>
        </div>
        <div class="setting-line">
          <el-input
            v-model="newPwd"
            placeholder="请输入新的密码"
            show-password
            @keypress.enter.native="clickSetPwd"
          ></el-input>&emsp;
          <el-button type="primary" plain @click="clickSetPwd" :disabled="showPwd2">修改</el-button>
        </div>
      </div>
      <div :class="pwdStyle">
        <div class="setting-line-no">
          <div class="setting-label">
            <span class="label-1">确认</span>
            <span class="label-2">密码</span>
          </div>
          <div class="tips">再输一遍 !!!</div>
        </div>
        <div class="setting-line">
          <el-input
            ref="pwd2"
            v-model="newPwd2"
            placeholder="请确认密码"
            show-password
            @keypress.enter.native="clickSetPwdTwice"
          ></el-input>&emsp;
          <el-button type="primary" plain @click="clickSetPwdTwice">确认</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { setTimeout } from 'timers'
export default {
  name: 'setting',
  data() {
    return {
      editable: false,
      newName: '',
      newPwd: '',
      newPwd2: '', // 确认密码
      pwdStyle: 'confirm-pwd',
      showPwd2: false // 是否展示确认密码框
    }
  },
  computed: {
    account() {
      return this.$store.state.account
    },
    name() {
      return this.$store.state.name
    },
    assertSmall() {
      return this.$store.state.ssize === 0
    }
  },
  methods: {
    showPwdDiv() {
      this.showPwd2 = true
      this.pwdStyle = 'confirm-pwd-show'
      // 切换input焦点
      // 这里避免了已经设置了焦点但是元素还没出现的尴尬
      setTimeout(() => {
        this.$refs.pwd2.focus()
      }, 500)
    },
    hidePwdDiv() {
      this.showPwd2 = false
      this.pwdStyle = 'confirm-pwd-hide'
    },
    clickSetName() {
      if (this.newName.length === 0) {
        this.$message.info('用户名不能为空')
        return
      }
      var newName = this.newName
      this.$post('/api/setname', {
        name: newName
      })
        .then(() => {
          this.$store.commit('setName', newName)
          this.$message.success('修改成功')
          this.newName = ''
        })
        .catch(err => {
          this.$message.error('修改失败, ' + err)
        })
    },
    clickSetPwd() {
      if (this.newPwd.length < 6) {
        this.$message.info('至少输入6位密码')
        return
      }
      this.showPwdDiv()
    },
    clickSetPwdTwice() {
      if (this.newPwd !== this.newPwd2) {
        this.$message.error('两次密码不一致')
      } else {
        // 提交修改的密码
        this.$post('/api/setpwd', {
          password: this.newPwd
        })
          .then(() => {
            this.$message.success('修改成功')
            this.hidePwdDiv()
            this.newPwd = ''
            this.newPwd2 = ''
          })
          .catch(err => {
            this.$message.error('修改失败, ' + err)
          })
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '../../assets/css/default';

.setting-box {
  width: 80%;
  min-width: 300px;
  max-width: 500px;
  margin: 50px auto;
}

.single-line {
  padding-top: 10px;
  margin-bottom: 10px;
  border-bottom: 1px solid #dedede;
}

.setting-line {
  display: flex;
  display: -webkit-flex;
  justify-content: space-between;
  align-items: center;
}

.setting-line-no {
  display: flex;
  display: -webkit-flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 2px;
}

.setting-label {
  .label-1 {
    font-size: 1rem;
    color: #909399;
  }

  .label-2 {
    color: #707377;
    font-size: 1.375rem;
    font-weight: bold;
    // text-decoration: underline;
  }
}

.tips-box {
  margin-bottom: 15px;
}

.tips {
  text-align: right;
  font-size: 0.75rem;
  color: #909399;
}

.setting-value {
  text-align: right;
  color: theme_color;
  font-weight: bold;
  font-size: 1.75rem;
  margin-bottom: 1px;
}

.name-input {
  // padding: 20px 0 0;
  margin-top: 60px;
}

.pwd-input {
  margin-top: 30px;
}

@keyframes pwd-show {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pwd-hide {
  to {
    opacity: 0;
    transform: translateY(30px);
  }
}

.confirm-pwd {
  visibility: hidden;
}

.confirm-pwd-show {
  animation: pwd-show 0.6s forwards;
}

.confirm-pwd-hide {
  margin-top: 10px;
  animation: pwd-hide 0.6s forwards;
}
</style>
