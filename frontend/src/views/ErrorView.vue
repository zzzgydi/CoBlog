<template>
  <div class="error-cnt">
    <h1>
      Random
      <br v-if="assertSmall" />
      <span>Error</span> Page
    </h1>
    <div class="layout">
      <h2>404</h2>
      <h3>
        Oops!
        <br v-if="assertSmall" />Page Not Found
      </h3>
    </div>
    <div class="back-link" @click="ClickBack">
      <i class="el-icon-back"></i>
      Go back&ensp;
    </div>
  </div>
</template>

<script>
export default {
  name: 'error',
  computed: {
    assertSmall() {
      return this.$store.state.ssize === 0
    }
  },
  methods: {
    ClickBack() {
      this.$router.go(-1)
    }
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/view.styl"></style>
