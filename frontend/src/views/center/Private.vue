<template>
  <div>
    <book :home="false" posturl="/api/usernotes" poststate="self"></book>
  </div>
</template>

<script>
import BookCommonVue from '../../components/BookCommon.vue'

export default {
  components: {
    book: BookCommonVue
  }
}
</script>
