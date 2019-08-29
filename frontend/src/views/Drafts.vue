<template>
  <div>
    <div>
      <div v-for="note in notes" :key="note.id" class="note-box">
        <div class="note-layout">
          <div class="note-title" @click="viewNote(note)">{{note.title || '未设置标题' }}</div>
          <el-dropdown @command="(cmd) => handleOption(cmd, note.id)" trigger="click">
            <el-button icon="el-icon-setting" plain size="small" circle></el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="revise">修改</el-dropdown-item>
              <el-dropdown-item command="remove">删除</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
        <div class="note-layout" @click="viewNote(note)">
          <div class="note-label">
            <el-tag type="danger">{{note.label || '未分类'}}</el-tag>
          </div>
          <div class="note-time">{{note.modified}}</div>
        </div>
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
  methods: {
    parseTime(t) {
      t = new Date(parseInt(t * 1000))
      var year = t.getFullYear()
      var month = t.getMonth() + 1
      var date = t.getDate()
      var hour = t.getHours()
      var minute = t.getMinutes()
      return year + '-' + month + '-' + date + ' ' + hour + ':' + minute
    },
    handleOption(cmd, id) {
      console.log(cmd, id)
      if (cmd === 'revise') {
        this.$router.push({ name: 'edit', params: { noteid: id } })
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
      state: 'temp'
    }).then(res => {
      for (let i in res.notes) {
        res.notes[i].modified = this.parseTime(res.notes[i].modified)
      }
      this.notes = res.notes
    })
  }
}
</script>

<style lang="stylus" scoped>
@import '../assets/default';

.note-box {
  width: 60%;
  cursor: pointer;
  margin: 0 auto 30px;
  padding: 1.5%;
  box-shadow: 0 1px 5px 0 rgba(0, 0, 0, 0.1);

  &:hover {
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  }
}

.note-layout {
  display: flex;
  display: -webkit-flex;
  justify-content: space-between;
  align-items: center;
}

.note-title {
  width: 90%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: default_black;
  font-size: 1.5rem;
  line-height: 50px;
}

.note-time {
  color: #909399;
}
</style>
