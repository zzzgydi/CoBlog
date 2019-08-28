<template>
  <div>
    <div>这里显示用户所有的笔记</div>
    <div>
      <div v-for="note in notes" :key="note.id">
        <div>{{note.label}}</div>
        <div>{{note.title}}</div>
        <div>{{note.modified}}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      notes: []
    }
  },
  beforeMount() {
    this.$post(
      '/api/getnotes',
      {
        state: 'save'
      },
      res => {
        this.notes = res.notes
        console.log(res)
      }
    )
  }
}
</script>

<style lang="stylus" scoped></style>