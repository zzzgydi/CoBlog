<template>
  <div>
    <book :home="false" posturl="/api/usernotes" poststate="temp"></book>
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
