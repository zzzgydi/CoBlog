<template>
  <div class="home">
    <div>这是首页</div>
  </div>
</template>

<script>
export default {
  name: 'home',
  components: {},
  methods: {
    handle() {
      this.$store.commit('change', true)
    }
  }
}
</script>

<style lang="stylus" scoped></style>
