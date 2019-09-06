<template>
  <!-- 首页的展示 -->
  <div class="note-box-vue">
    <div @click="viewNote">
      <div class="note-title-vue">
        <el-tag type="primary" size="mini">{{note.label}}</el-tag>
        <div class="title">{{note.title}}</div>
      </div>
      <p class="note-content-vue">{{note.content}}...</p>
      <div class="note-time-vue">
        <span>{{note.modified}}</span>
        <span>&ensp;|&ensp;</span>
        <span>{{note.author}}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['note'],
  data() {
    return {}
  },
  methods: {
    viewNote() {
      this.$router.push({
        path: '/view/' + this.note.nid
      })
    }
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/book.styl"></style>
