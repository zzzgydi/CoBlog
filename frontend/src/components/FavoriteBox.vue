<template>
  <div class="fav-box-vue">
    <!-- 收藏夹的每一项 -->
    <a @click="clickItem" :href="favurl.url" target="_blank">
      <div class="fav-title">
        <el-tag size="mini">URL</el-tag>
        <span>&ensp;{{favurl.title}}</span>
      </div>
      <p class="fav-content">{{favurl.remark}}</p>
      <div class="fav-time">{{favurl.modified}}</div>
    </a>
  </div>
</template>

<script>
export default {
  props: ['favurl'],
  data() {
    return {}
  },
  methods: {
    clickItem() {
      // window.open(this.favurl.url, '_blank')
    }
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/favorite.styl"></style>
