<template>
  <div class="home-cnt">
    <div class="note-head-small" v-if="assertSmall">
      <el-input size="small" v-model="searchFilter" placeholder="输入关键词" clearable></el-input>
      <el-button size="small" @click="showPicker=true">Filter</el-button>
      <van-popup v-model="showPicker" position="bottom">
        <van-picker
          show-toolbar
          @cancel="showPicker = false"
          @confirm="pickerSelect"
          :columns="labelOptions"
        />
      </van-popup>
    </div>
    <div class="home-note-box">
      <div class="home-filter-box" v-if="!assertSmall">
        <el-input size="mini" v-model="searchFilter" placeholder="输入关键词" clearable></el-input>
        <span>&emsp;</span>
        <el-select size="mini" v-model="selectFilter" clearable>
          <el-option v-for="item in labelOptions" :key="item" :label="item" :value="item"></el-option>
        </el-select>
      </div>
      <div
        v-for="note in notesFilter"
        :key="note.id"
        class="home-note-each"
        @click="viewNote(note)"
      >
        <div class="home-note-title">
          <el-tag type="primary" size="mini">{{note.label}}</el-tag>
          <div class="title">{{note.title}}</div>
        </div>
        <p class="home-note-content">{{note.content}}...</p>
        <div class="home-note-time">
          <span>{{note.modified}}</span>
          <span>&ensp;|&ensp;</span>
          <span>{{note.author}}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Tool from '../assets/js/tool'

export default {
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
  methods: {
    viewNote(note) {
      this.$router.push({
        path: '/view/' + note.id
      })
    },
    pickerSelect(value, index) {
      this.selectFilter = value
      this.showPicker = false
    }
  },
  beforeMount() {
    this.$post('/api/getnotes', {
      state: 'save'
    }).then(res => {
      var options = new Set()
      for (let i in res.notes) {
        res.notes[i].modified = Tool.parseTime(res.notes[i].modified)
        res.notes[i].label = res.notes[i].label.trim() || '未分类'
        res.notes[i].title = res.notes[i].title || '未设置标题'
        res.notes[i].author = res.notes[i].author || '未命名'
        options.add(res.notes[i].label)
      }
      this.notes = res.notes
      this.labelOptions = [...options]
    })
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/book.styl"></style>
