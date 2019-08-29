<template>
  <div>
    <book :home="false"></book>
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
