<template>
  <div class="note-cnt">
    <div class="filter-box">
      <el-input v-model="searchFilter" style="width:200px;" placeholder="输入关键词" clearable></el-input>
      <span>&emsp;&emsp;</span>
      <el-select v-model="selectFilter" clearable style="width:200px;">
        <el-option v-for="item in labelOptions" :key="item" :label="item" :value="item"></el-option>
      </el-select>
    </div>

    <div class="note-box">
      <div v-for="note in notesFilter" :key="note.id" class="note-each-box">
        <div class="note-layout">
          <div class="note-tag-title" @click="viewNote(note)">
            <el-tag type="danger" size="mini">{{note.label || '未分类'}}</el-tag>
            <div class="note-title">{{note.title || '未设置标题' }}</div>
          </div>
          <el-dropdown @command="(cmd) => handleOption(cmd, note.id)" trigger="click">
            <el-button icon="el-icon-setting" plain size="mini" circle></el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="revise">修改</el-dropdown-item>
              <el-dropdown-item command="remove">删除</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
        <div class="note-content" @click="viewNote(note)">{{note.content}}...</div>
        <div class="note-layout" @click="viewNote(note)">
          <div class="note-time">{{note.modified}}</div>
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
      labelOptions: []
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
    }
  },
  methods: {
    handleOption(cmd, id) {
      if (cmd === 'revise') {
        this.$router.push({ name: 'edit', params: { noteid: id } })
      } else if (cmd === 'remove') {
        this.$post('/api/notestate', { noteid: id, state: 'del' }).then(() => {
          var i = 0
          for (i = 0; i < this.notes.length; ++i) {
            if (this.notes[i].id === id) break
          }
          this.notes.splice(i, 1)
          this.$message.success('删除成功')
        })
      }
    },
    viewNote(note) {
      this.$router.push({
        path: '/view/' + note.id
      })
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
        options.add(res.notes[i].label)
      }
      this.notes = res.notes
      this.labelOptions = [...options]
    })
  }
}
</script>

<style lang="stylus" scoped>
@import '../assets/default';

.note-cnt {
  width: 60%;
  margin: 0 auto 40px;
}

.filter-box {
  text-align: right;
  margin-bottom: 20px;

  span {
    noselect();
  }
}

.note-box {
  background-color: #fff;
  box-shadow: 0 0px 5px 0 rgba(0, 0, 0, 0.1);
}

.note-each-box {
  cursor: pointer;
  padding: 1.5% 2.5%;
  border-bottom: 1px solid #efefee;

  &:hover {
    box-shadow: 0px 0px 8px 0 rgba(0, 0, 0, 0.1);

    .note-title {
      color: theme_color;
    }
  }
}

.note-layout {
  display: flex;
  display: -webkit-flex;
  justify-content: space-between;
  align-items: center;
}

.note-tag-title {
  display: flex;
  display: -webkit-flex;
  align-items: center;
  width: 88%;

  .note-title {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    color: default_black;
    font-size: 1rem;
    font-weight: bold;
    margin-left: 8px;
  }
}

.note-content {
  font-size: 0.875rem;
  color: #6f6f6f;
  // margin-top: 4px;
}

.note-time {
  // font-size: 0.875rem;
  color: #909399;
  margin-top: 4px;
}
</style>
