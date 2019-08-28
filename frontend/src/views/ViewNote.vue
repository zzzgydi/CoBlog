<template>
  <div class="edit">
    <br />
    <mavon-editor v-model="value" :subfield="false" defaultOpen="preview" :toolbarsFlag="false" />
    <mavon-editor v-model="value" style="height: 400px;" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      value: '# hello\n## 1胡塞但是'
    }
  }
}
</script>

<style lang="stylus" scoped>
.edit {
  width: 800px;
  margin: 0 auto;
}
</style>