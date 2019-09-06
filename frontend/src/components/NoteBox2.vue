<template>
  <!-- 其他页面的展示 -->
  <div class="note-box-vue note-box-vue2">
    <div @click="viewNote">
      <div class="note-title-vue">
        <el-tag :type="tagStyle" size="mini">{{note.label}}</el-tag>
        <div class="title">{{note.title}}</div>
      </div>
      <p class="note-content-vue">{{note.content}}...</p>
      <div class="note-time-vue">
        <span>{{note.modified}}</span>
      </div>
    </div>
    <!-- 选项层触发器 -->
    <div class="note-btn-trigger" v-show="!visible">
      <el-button
        @click="showOptions"
        :type="tagStyle"
        icon="el-icon-setting"
        plain
        size="small"
        circle
      ></el-button>
    </div>
    <!-- 选项层 -->
    <div
      class="note-btn-cnt"
      :class="optionClass"
      @mouseenter="handleEnter"
      @mouseleave="handleLeave"
    >
      <!-- 回收站的选项 -->
      <div class="note-btn-box" v-if="recycle">
        <div class="first-btn">
          <el-button size="small" type="primary" plain @click="clickRestore">还原</el-button>
        </div>
        <div class="btn">
          <el-button size="small" type="danger" plain @click="clickRemove">移除</el-button>
        </div>
      </div>
      <!-- 其他界面的选项 -->
      <div class="note-btn-box" v-else>
        <div class="first-btn">
          <el-button size="small" type="primary" plain @click="clickEdit">编辑</el-button>
        </div>
        <div class="btn">
          <el-button size="small" type="danger" plain @click="clickDelete">删除</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['note', 'recycle', 'tagStyle'],
  data() {
    return {
      visible: null,
      timeout: null
    }
  },
  computed: {
    optionClass() {
      if (this.visible) return 'note-btn-show'
      else if (this.visible === false) return 'note-btn-hide'
      return 'note-btn-null' // 避免首次加载时动画闪过
    }
  },
  methods: {
    viewNote() {
      this.$router.push({
        path: '/view/' + this.note.nid
      })
    },
    showOptions() {
      // 弹出选项框
      this.visible = true
      this.timeout = setTimeout(() => {
        this.visible = false
      }, 1250)
    },
    clickEdit() {
      this.$router.push({ name: 'edit', params: { noteid: this.note.nid } })
    },
    clickDelete() {
      // 放入回收站
      this.$post('/api/notestate', {
        noteid: this.note.nid,
        state: 'del'
      })
        .then(() => {
          this.$message.success('删除成功')
          this.$emit('delItem', this.note.nid)
        })
        .catch(err => {
          this.$message.error('删除失败 ' + err)
        })
    },
    clickRestore() {
      // 从回收站放回草稿箱中
      this.$post('/api/notestate', {
        noteid: this.note.nid,
        state: 'temp'
      })
        .then(() => {
          this.$message.success('还原成功')
          this.$emit('delItem', this.note.nid)
        })
        .catch(err => {
          this.$message.error('还原失败 ' + err)
        })
    },
    clickRemove() {
      // 回收站界面 - 永久删除
      this.$confirm('是否确认永久删除该笔记', '提示')
        .then(() => {
          this.$post('/api/delnote', { noteid: this.note.nid })
            .then(() => {
              // 调用父组件的方法
              this.$message.success('删除成功')
              this.$emit('delItem', this.note.nid)
            })
            .catch(err => {
              this.$message.error('删除失败 ' + err)
            })
        })
        .catch(e => e)
    },
    handleEnter() {
      if (this.timeout) clearTimeout(this.timeout)
    },
    handleLeave() {
      this.timeout = setTimeout(() => {
        this.visible = false
      }, 500)
    }
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/book.styl"></style>
