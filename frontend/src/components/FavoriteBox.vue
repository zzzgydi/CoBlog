<template>
  <div class="fav-box-vue">
    <!-- 收藏夹的每一项 -->
    <el-popover placement="top-start" trigger="hover" :content="favurl.url" :open-delay="500">
      <a slot="reference" :href="favurl.url" target="_blank">
        <div class="fav-title">
          <el-tag size="mini">URL</el-tag>
          <span>&ensp;{{favurl.title}}</span>
        </div>
        <p class="fav-content">{{favurl.remark}}</p>
        <div class="fav-time">{{favurl.modified}}</div>

        <div class="fav-del-btn">
          <el-button
            @click.prevent="deleteItem"
            size="small"
            plain
            circle
            type="danger"
            icon="el-icon-delete"
          ></el-button>
        </div>
      </a>
    </el-popover>
  </div>
</template>

<script>
export default {
  props: ['favurl'],
  data() {
    return {}
  },
  methods: {
    deleteItem() {
      this.$confirm('是否确认删除该链接', '提示')
        .then(() => {
          this.$post('/api/delurl', { fid: this.favurl.fid }).then(() => {
            this.$emit('delItem', this.favurl.fid)
            setTimeout(() => this.$message.success('删除成功'), 250)
          })
        })
        .catch(e => e)
    }
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/favorite.styl"></style>
<style>
.el-popover--plain {
  padding: 10px;
}
</style>
