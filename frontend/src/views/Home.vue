<template>
  <div class="home">
    <div></div>
  </div>
</template>

<script>
// @ is an alias to /src

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
