<template>
  <div class="setting-cnt">
    <card-box title="个人信息" style="margin-bottom:20px;">
      <card-line label="头像">
        <avatar style="float:right"></avatar>
      </card-line>
      <card-line style="margin-top:10px" label="账号" :value="account"></card-line>
      <card-line style="margin-top:10px" label="用户名" :value="name"></card-line>
    </card-box>
    <!-- 主页设置 -->
    <card-box title="主页设置" style="margin-bottom:20px;">
      <card-line label="启用主页跳转">
        <el-switch v-model="flag" @change="flagChange"></el-switch>
      </card-line>
      <card-line label="跳转地址" style="margin-top:15px">
        <el-input :disabled="!flag" v-model="alias" placeholder="请输入跳转地址" class="alias-input">
          <el-button slot="append" icon="el-icon-check" @click="setAlias"></el-button>
        </el-input>
      </card-line>
    </card-box>
    <!-- 修改信息栏不大改了 -->
    <card-box title="修改信息">
      <div class="setting-line-no">
        <div class="setting-label">修改用户名</div>
        <div class="tips">有字就行...</div>
      </div>
      <div class="setting-line">
        <el-input v-model="newName" placeholder="请输入新的用户名" @keypress.enter.native="clickSetName"></el-input>&emsp;
        <el-button type="primary" plain @click="clickSetName">修改</el-button>
      </div>
      <div class="setting-line-no margin-top-20">
        <div class="setting-label">修改密码</div>
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
      <div class="confirm-pwd" :class="pwdStyle">
        <div class="setting-line-no margin-top-20">
          <div class="setting-label">确认密码</div>
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
    </card-box>
  </div>
</template>

<script>
import CardBoxVue from '../../components/small/CardBox.vue'
import AvatarVue from '../../components/small/Avatar.vue'
import CardLineVue from '../../components/small/CardLine.vue'
import Tool from '../../assets/js/tool'

// 防抖
function debounce(func, wait) {
  let timeout
  return function() {
    let context = this
    let args = arguments

    if (timeout) clearTimeout(timeout)

    timeout = setTimeout(() => {
      func.apply(context, args)
    }, wait)
  }
}

export default {
  name: 'setting',
  components: {
    'card-box': CardBoxVue,
    'card-line': CardLineVue,
    avatar: AvatarVue
  },
  data() {
    return {
      editable: false,
      newName: '',
      newPwd: '',
      newPwd2: '', // 确认密码
      pwdStyle: '',
      showPwd2: false, // 是否展示确认密码框
      imageUrl: '',
      flag: !!this.$store.state.flag, // 是否启用主页跳转
      alias: this.$store.state.alias // 跳转地址
    }
  },
  computed: {
    account() {
      return this.$store.state.account
    },
    name() {
      return this.$store.state.name || '未命名'
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
        this.$message.error('密码不一致')
      } else {
        // 提交修改的密码
        this.$post('/api/setpwd', {
          password: Tool.encrypt(this.newPwd)
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
    },
    setAlias() {
      if (!Tool.checkUrl(this.alias)) {
        this.$message.info('请输入有效链接')
        return
      }
      this.$post('/api/page/setalias', { alias: this.alias })
        .then(res => {
          this.$message.success('设置成功')
        })
        .catch(() => {
          this.$message.error('设置出错')
        })
    },
    flagChange: debounce(function(val) {
      // 上传修改flag配置
      this.$post('/api/page/setflag', { flag: val }).then(() => {
        let msg = val ? '启用成功' : '已关闭'
        this.$message.success(msg)
        this.$store.commit('setUser', { flag: val })
      })
    }, 500)
  }
}
</script>

<style lang="stylus" scoped src="../../assets/css/view.styl"></style>
