<template>
  <div class="catalogue-cnt">
    <div class="label-box" v-for="(label, idx) in notes" :key="idx">
      <div class="label">&ensp;{{idx}}</div>
      <div class="note-box" v-for="note in notes[idx]" :key="note.id">
        <div class="note-title" @click="viewNote(note)">&emsp;&ensp;{{note.title || '未设置标题' }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      notes: {}
    }
  },
  methods: {
    viewNote(note) {
      let path = '/view/' + note.id
      if (this.$route.path === path) return
      this.$router.push(path)
    }
  },
  beforeMount() {
    this.$post('/api/getnotes', {
      state: 'save'
    }).then(res => {
      this.notes = {}
      for (let i in res.notes) {
        let l = res.notes[i].label || '未分类'
        if (!this.notes[l]) this.notes[l] = []
        //   res.notes[i].modified = this.parseTime(res.notes[i].modified)
        this.notes[l].push(res.notes[i])
      }
    })
  }
}
</script>

<style lang="stylus" scoped>
@import '../assets/default';

line_margin = 8px;

.catalogue-cnt {
  width: 100%;
  box-shadow: 0 1px 5px 0 rgba(0, 0, 0, 0.1);
  padding: 15px 10px;
  color: default_black;
}

.label-box {
  border-bottom: 1px solid #eee;
  margin-bottom: line_margin;
  padding-bottom: line_margin;

  &:last-child {
    margin-bottom: 0px;
    border-bottom: none;
    padding-bottom: 0px;
  }

  .label {
    font-size: 1.12rem;
    color: #a0a3a9;
  }

  .note-box {
    line-height: 30px;

    &:hover {
      // box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
      color: theme_color;
    }
  }

  .note-title {
    cursor: pointer;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    // font-weight: bold;
  }
}
</style>
