<template>
  <div class="setting-cnt">
    <h3>个人信息</h3>
    <div>
      <div>
        <span>账号:</span>
        <span>{{account}}</span>
      </div>
      <div>
        <span>用户名:</span>
        <span>{{name}}</span>
      </div>
      <el-input v-model="newName" placeholder="输入新的用户名"></el-input>
      <el-button @click="clickSetName">确认修改</el-button>

      <el-input v-model="newPwd" placeholder="输入新的密码" show-password></el-input>
      <el-button @click="clickSetPwd">确认修改</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'setting',
  data() {
    return {
      editable: false,
      newName: '',
      newPwd: ''
    }
  },
  computed: {
    account() {
      return this.$store.state.account
    },
    name() {
      return this.$store.state.name
    }
  },
  methods: {
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
        })
        .catch(err => {
          this.$message.error('修改失败')
          console.log(err)
        })
    },
    clickSetPwd() {
      if (this.newPwd.length < 6) {
        this.$message.info('至少输入6位密码')
        return
      }
      var newPwd = this.newPwd
      this.$post('/api/setpwd', {
        password: newPwd
      })
        .then(() => {
          this.$message.success('修改成功')
        })
        .catch(err => {
          this.$message.error('修改失败')
          console.log(err)
        })
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '../../assets/css/default';

.setting-cnt {
  width: 65%;
  min-width: 300px;
  margin: 40px auto;
  background-color: #fefefe;
  padding: 30px 40px;

  h3 {
    color: #909399;
  }
}
</style>
