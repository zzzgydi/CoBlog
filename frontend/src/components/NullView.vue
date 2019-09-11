<template>
  <div class="null-box">
    <div class="null-head">
      <span>Empty List</span>
    </div>
    <div class="go-link" @click="gotoEdit">
      <span v-if="fav">add favorites&ensp;</span>
      <span v-else>make note&ensp;</span>
      <i class="el-icon-right"></i>
    </div>
  </div>
</template>

<script>
export default {
  props: ['fav'],
  methods: {
    gotoEdit() {
      if (this.fav) this.$router.push('/center/editfav')
      else this.$router.push('/center/edit')
    }
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/view.styl"></style>
