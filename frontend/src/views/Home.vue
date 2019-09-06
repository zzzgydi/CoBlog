<template>
  <div class="home-cnt">
    <!-- 头部过滤器 -->
    <div class="note-option-cnt">
      <div class="note-option-filter">
        <div class="note-option-input">
          <span>关键词&ensp;</span>
          <el-input class="note-input" v-model="searchFilter" placeholder="输入关键词" clearable></el-input>
        </div>
        <div class="note-option-select">
          <span v-if="!assertSmall">标签&ensp;</span>
          <span v-else>标&emsp;签&ensp;</span>
          <el-select class="note-input" v-model="selectFilter" clearable>
            <el-option v-for="item in labelOptions" :key="item" :label="item" :value="item"></el-option>
          </el-select>
        </div>
      </div>
    </div>
    <div v-for="note in notesFilter" :key="note.id">
      <note-box :note="note"></note-box>
    </div>
  </div>
</template>

<script>
import Tool from '../assets/js/tool'
import NoteBoxVue from '../components/NoteBox.vue'

export default {
  components: {
    'note-box': NoteBoxVue
  },
  data() {
    return {
      notes: [],
      searchFilter: '',
      selectFilter: '',
      labelOptions: [],
      showPicker: false // 显示popup
    }
  },
  computed: {
    notesFilter() {
      if (!(this.searchFilter || this.selectFilter)) return this.notes
      var selectList, searchList
      if (this.selectFilter) {
        selectList = this.notes.filter(n => n.label === this.selectFilter)
        if (!this.searchFilter) return selectList
      }
      if (this.searchFilter) {
        searchList = this.notes.filter(
          n => n.title.indexOf(this.searchFilter) !== -1
        )
        if (!this.selectFilter) return searchList
      }
      return Tool.arrayIntersection(selectList, searchList)
    },
    assertSmall() {
      return this.$store.state.ssize === 0
    }
  },
  methods: {},
  beforeMount() {
    this.$post('/api/getnotes', {
      state: 'save'
    }).then(res => {
      var options = new Set()
      for (let i in res.notes) {
        res.notes[i].modified = Tool.parseTime(res.notes[i].modified)
        res.notes[i].label = res.notes[i].label.trim() || '未分类'
        res.notes[i].title = res.notes[i].title || '未设置标题'
        res.notes[i].author = res.notes[i].name || '未命名'
        options.add(res.notes[i].label)
      }
      this.notes = res.notes
      this.labelOptions = [...options]
    })
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/book.styl"></style>
