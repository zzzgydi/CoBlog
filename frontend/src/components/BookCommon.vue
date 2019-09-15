<template>
  <div class="note-cnt">
    <div>
      <div class="note-option-cnt">
        <div class="note-option-title" v-show="!assertSmall">
          <i :class="page.icon"></i>
          <span>{{page.name}}</span>
        </div>
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
      <div :hidden="isNullView" v-for="note in notesFilter" :key="note.nid">
        <note-box
          :note="note"
          @delItem="delNoteHere"
          :recycle="page.hideBtn"
          :tagStyle="page.tagStyle"
          :mine="page.poststate==='mine'"
        ></note-box>
      </div>
    </div>

    <null-view :hidden="!isNullView"></null-view>
  </div>
</template>

<script>
import Tool from '../assets/js/tool'
import NullViewVue from './NullView.vue'
import NoteBox2Vue from './box/NoteBox2.vue'

export default {
  name: 'bookcommon',
  props: ['page'],
  components: {
    'null-view': NullViewVue,
    'note-box': NoteBox2Vue
  },
  data() {
    return {
      notes: [],
      searchFilter: '',
      selectFilter: '',
      labelOptions: [],
      isNullView: false
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
    updateData() {
      this.selectFilter = ''
      this.searchFilter = ''

      this.$post(this.page.posturl, {
        state: this.page.poststate
      })
        .then(res => {
          if (res.notes.length < 1) {
            this.isNullView = true
            return
          }
          var options = new Set()
          for (let i in res.notes) {
            res.notes[i].modified = Tool.parseTime(res.notes[i].modified)
            res.notes[i].label = res.notes[i].label.trim() || '未分类'
            res.notes[i].title = res.notes[i].title || '未设置标题'
            options.add(res.notes[i].label)
          }
          this.notes = res.notes
          this.labelOptions = [...options]
          this.isNullView = false
        })
        .catch(() => {
          this.isNullView = true
        })
    },
    delNoteHere(nid) {
      // 对组件元素内的数组元素进行删除
      var i = 0
      for (i = 0; i < this.notes.length; ++i) {
        if (this.notes[i].nid === nid) break
      }
      this.notes.splice(i, 1)
      if (this.notes.length < 1) {
        this.isNullView = true
      }
    }
  },
  watch: {
    '$route.path': function() {
      this.updateData()
    }
  },
  beforeMount() {
    this.updateData()
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/book.styl"></style>
