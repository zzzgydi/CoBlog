<template>
  <div class="note-cnt">
    <div class="note-head-small" v-if="assertSmall && !isNullView">
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
    <div class="note-box" :hidden="isNullView">
      <div class="note-head" v-show="!assertSmall">
        <div class="book-head">
          <i :class="page.icon"></i>
          {{page.name}}
        </div>
        <div class="filter-box">
          <el-input size="mini" v-model="searchFilter" placeholder="输入关键词" clearable></el-input>
          <span>&emsp;</span>
          <el-select size="mini" v-model="selectFilter" clearable>
            <el-option v-for="item in labelOptions" :key="item" :label="item" :value="item"></el-option>
          </el-select>
        </div>
      </div>
      <div v-for="note in notesFilter" :key="note.id" class="note-each">
        <div class="click-view" @click="viewNote(note)">
          <div class="note-title">
            <el-tag type="danger" size="mini">{{note.label}}</el-tag>
            <div class="title">{{note.title}}</div>
          </div>
          <div class="note-content">{{note.content}}...</div>
          <div class="note-time">{{note.modified}}</div>
        </div>
        <div class="btn-view">
          <div v-if="!page.hideBtn">
            <el-dropdown @command="(cmd) => handleOption(cmd, note.id)" trigger="click">
              <el-button icon="el-icon-setting" plain size="mini" circle></el-button>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="revise">编辑</el-dropdown-item>
                <el-dropdown-item command="remove">删除</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </div>
          <div v-else>
            <el-button
              type="danger"
              plain
              icon="el-icon-delete"
              size="mini"
              circle
              @click="deleteNote(note.id)"
            ></el-button>
          </div>
        </div>
      </div>
    </div>

    <null-view :hidden="!isNullView"></null-view>
  </div>
</template>

<script>
import Tool from '../assets/js/tool'
import NullViewVue from './NullView.vue'

export default {
  name: 'bookcommon',
  props: ['page'],
  components: {
    'null-view': NullViewVue
  },
  data() {
    return {
      notes: [],
      searchFilter: '',
      selectFilter: '',
      labelOptions: [],
      isNullView: false,
      showPicker: false
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
    // assertMini() {
    //   return this.$store.state.ssize === -1
    // },
    assertSmall() {
      return this.$store.state.ssize === 0
    }
    // assertMedium() {
    //   return this.$store.state.ssize === 1
    // },
    // assertLarge() {
    //   return this.$store.state.ssize === 2
    // }
  },
  methods: {
    updateData() {
      this.selectFilter = ''
      this.searchFilter = ''
      this.showPicker = false

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
    delNoteHere(id) {
      // 对组件元素内的数组元素进行删除
      var i = 0
      for (i = 0; i < this.notes.length; ++i) {
        if (this.notes[i].id === id) break
      }
      this.notes.splice(i, 1)
      this.$message.success('删除成功')
      if (this.notes.length < 1) {
        this.isNullView = true
      }
    },
    handleOption(cmd, id) {
      if (cmd === 'revise') {
        this.$router.push({ name: 'edit', params: { noteid: id } })
      } else if (cmd === 'remove') {
        this.$post('/api/notestate', { noteid: id, state: 'del' }).then(() => {
          this.delNoteHere(id)
        })
      }
    },
    deleteNote(id) {
      // 回收站界面 - 永久删除
      this.$confirm('是否确认永久删除该笔记', '提示').then(() => {
        this.$post('/api/delnote', { noteid: id }).then(() => {
          this.delNoteHere(id)
        })
      })
    },
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
