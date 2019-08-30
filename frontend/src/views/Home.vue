<template>
  <div class="home">
    <book :home="true" posturl="/api/getnotes" poststate="save"></book>
  </div>
</template>

<script>
import BookCommonVue from '../components/BookCommon.vue'

export default {
  name: 'home',
  components: {
    book: BookCommonVue
  },
  methods: {}
}
</script>

<style lang="stylus" scoped></style>
