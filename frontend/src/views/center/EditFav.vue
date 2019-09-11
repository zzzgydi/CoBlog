<template>
  <div class="favedit-cnt">
    <div class="favedit-box">
      <div class="fav-item">
        <span>标题&ensp;</span>
        <el-input v-model="title" placeholder="请输入链接标题"></el-input>
      </div>
      <div class="fav-item">
        <span>链接&ensp;</span>
        <el-input type="textarea" v-model="url" resize="none" placeholder="请输入需要收藏的链接"></el-input>
      </div>
      <div class="fav-item">
        <span>描述</span>
        <el-input type="textarea" :rows="5" v-model="desc" resize="none" placeholder="请输入对该链接的描述"></el-input>
      </div>
      <div class="btn-cnt">
        <el-button type="primary" plain @click="handleSubmit">提交</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      url: '',
      desc: ''
    }
  },
  methods: {
    reset() {
      this.title = ''
      this.url = ''
      this.desc = ''
    },
    handleSubmit() {
      if (this.title.length < 1) {
        this.$message.info('请输入标题')
        return
      }
      if (!this.checkUrl(this.url)) {
        this.$message.info('请输入有效链接')
        return
      }
      this.$post('/api/addurl', {
        title: this.title,
        url: this.url,
        desc: this.desc
      })
        .then(() => {
          this.$message.success('添加成功')
          this.reset()
        })
        .catch(e => {
          this.$message.error('添加失败 ' + e)
        })
    },
    checkUrl(url) {
      const re = /(https?|ftp|file):\/\/[-A-Za-z0-9+&@#\/%?=~_|!:,.;]+[-A-Za-z0-9+&@#\/%=~_|]/
      return re.test(url)
    }
  }
}
</script>

<style lang="stylus" scoped src="../../assets/css/favorite.styl"></style>
