<template>
  <!-- 个人主页的展示 -->
  <div class="note-box-vue">
    <router-link :to="'/view/' + note.nid">
      <div class="note-title-vue">
        <!-- <el-tag type="primary" size="mini">{{note.label}}</el-tag> -->
        <div class="title">{{note.title}}</div>
      </div>
      <p class="note-content-vue">{{note.content}}...</p>
      <div class="note-time-vue">
        <span>
          <i class="el-icon-view"></i>
          {{note.look}}&emsp;
        </span>
        <span>
          <i class="el-icon-collection-tag"></i>
          {{note.label}}
        </span>
        <span style="float:right">{{note.modified}}</span>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  props: ['note'],
  methods: {
    viewNote() {
      this.$router.push({
        path: '/view/' + this.note.nid
      })
    }
  }
}
</script>

<style lang="stylus" scoped src="../../assets/css/book.styl"></style>
