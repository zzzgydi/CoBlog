<template>
  <div class="editor-cnt">
    <div class="editor-head">
      <div class="editor-title">
        <span>标题&ensp;</span>
        <el-input class="title-input" v-model="title" placeholder="请输入标题"></el-input>
      </div>
      <div class="editor-select">
        <span>标签&ensp;</span>
        <el-select class="title-input" v-model="label" placeholder="未分类" @change="handleSelect">
          <el-option
            v-for="item in labelOptions"
            :key="item.l_id"
            :label="item.value"
            :value="item.value"
          >
            <span style="float:left">{{ item.value }}</span>
            <span style="float:right;color:#8492a6;" @click.stop="delLabel(item.l_id)">
              <i class="el-icon-close"></i>
            </span>
          </el-option>
          <el-option label="新建标签" value="__new__" style="text-align:center;">
            <span style="color:#6a67ce;">新建标签</span>
          </el-option>
        </el-select>
      </div>
      <div class="editor-option">
        <span>{{ispublic ? '公开' : '私密'}}&ensp;</span>
        <el-switch v-model="ispublic"></el-switch>
      </div>
    </div>
    <div :class="assertSmall?'editor-cnt-small':''">
      <my-editor
        ref="myeditor"
        v-model="content"
        @ctrls="handleSave('temp')"
        @finishUpload="$finishUpload"
      ></my-editor>
      <el-progress class="progress-cnt" v-show="showProgress" :percentage="percent"></el-progress>
    </div>
    <div class="btn-box" v-if="!assertSmall">
      <el-button type="info" plain @click="handleSave('temp')">草稿笔记</el-button>
      <el-button type="primary" plain @click="handleSave('save')">{{ispublic?'发布':'保存'}}</el-button>
    </div>

    <div class="btn-box-small" v-else>
      <el-button size="small" type="info" plain @click="handleSave('temp')">草稿笔记</el-button>
      <el-button
        size="small"
        type="primary"
        plain
        @click="handleSave('save')"
      >{{ispublic?'发布':'保存'}}</el-button>
    </div>

    <el-dialog title="新增标签" width="360px" :visible.sync="dialogVisible" @close="dialogClose">
      <el-input v-model="newLabel" clearable placeholder="请输入标签名称" @keyup.enter.native="addLabel"></el-input>
      <div style="margin-top:20px;text-align:center;">
        <el-button type="success" plain @click="addLabel" style="width:120px;">新增</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import MyEditorVue from '../../components/MyEditor.vue'

export default {
  name: 'editor',
  components: {
    'my-editor': MyEditorVue
  },
  data() {
    return {
      dialogVisible: false, // 对话框
      noteid: -1,
      title: '',
      label: '',
      content: '',
      ispublic: false,
      labelOptions: [],
      newLabel: '',
      percent: 0,
      showProgress: false,
      state: '',
      _state: '',

      submitState: 'new', // new/update 用于判断是更新笔记还是新建笔记
      old_title: '', // 用于缓存比较
      old_label: '', // 用于缓存比较
      old_content: '' // 用于缓存比较
    }
  },
  computed: {
    assertSmall() {
      return this.$store.state.ssize === 0
    }
  },
  methods: {
    resetField() {
      this.noteid = -1
      this.title = ''
      this.label = ''
      this.submitState = 'new'
      this.ispublic = false
      this.state = ''
      this.updateContent('')
      this.updateOld()
    },
    updateOld() {
      this.old_title = this.title
      this.old_label = this.label
      this.old_content = this.content
    },
    updateContent(val) {
      // 用于更新父子组件的内容
      this.content = val
      this.$refs.myeditor.mycontent = val
    },
    checkChange() {
      // 判断数据是否有变动
      return !(
        this.old_title === this.title &&
        this.old_label === this.label &&
        this.old_content === this.content
      )
    },
    handleSave(state) {
      if (this.title.trim().length === 0) {
        this.$message.error('请输入标题')
        return
      }
      // 对发布的内容进行一个小小的验证
      if (this.content.trim().length === 0 && state === 'save') {
        this.$message.error('请输入有效正文')
        return
      }
      // 转变为私人笔记
      if (state === 'save' && !this.ispublic) state = 'self'
      // 判断是否改变
      if (!this.checkChange(state) && this.state === state) return

      if (this.beginUploadImgs()) {
        this._state = state // 有图片需要上传 缓存state，等待子组件触发$finishUpload
      } else {
        this.postData(state) // 没有图片需要上传
      }
    },
    $finishUpload(errorNum) {
      // 图片全部上传完成, 触发数据上传
      console.log(errorNum)
      this.postData(this._state)
      this._state = '' // 避免有bug
      setTimeout(() => (this.showProgress = false), 1000)
    },
    beginUploadImgs() {
      // 检查是否有图片需要上传
      if (this.$refs.myeditor.checkImg()) {
        // 有则显示进度条
        this.showProgress = true
        // 开始上传图片
        this.$refs.myeditor.uploadAllImgs(obj => {
          this.percent = obj.progress
        })
        return true // 表示有图片需要上传
      }
      return false // 表示没有图片需要上传
    },
    postData(state) {
      // 负责上传数据
      var url = this.submitState === 'new' ? '/api/addnote' : '/api/updatenote'
      var msg =
        this.submitState === 'new'
          ? '是否确认发布新笔记？'
          : '是否确认修改笔记？'
      var params = {
        noteid: this.noteid,
        label: this.label,
        title: this.title,
        content: this.content,
        state: state
      }
      this.state = state
      if (state === 'save') {
        this.$confirm(msg, '提示')
          .then(() => {
            this.$post(url, params)
              .then(() => {
                this.resetField() // 发布的内容就清空
                setTimeout(() => this.$message.success('提交成功'), 250)
              })
              .catch(() => this.$message.error('提交失败'))
          })
          .catch(err => err)
      } else if (state === 'temp') {
        this.$post(url, params)
          .then(() => {
            this.submitState = 'update' // 这里我不清空内容
            this.updateOld()
            this.$message.success('成功保存至草稿箱')
          })
          .catch(() => this.$message.error('保存失败'))
      } else if (state === 'self') {
        this.$post(url, params)
          .then(() => {
            this.resetField() // 发布的内容就清空
            this.$message.success('成功提交到私人笔记')
          })
          .catch(() => this.$message.error('提交失败'))
      } else {
        this.$message.error('UnHandled Error')
      }
    },
    handleSelect(value) {
      if (value === '__new__') this.dialogVisible = true
    },
    dialogClose() {
      if (this.label === '__new__') {
        this.label = ''
        this.newLabel = ''
      }
    },
    getLabels() {
      // 获取所有的标签
      this.$post('/api/getlabels').then(res => {
        this.labelOptions = res.labels
      })
    },
    addLabel() {
      this.newLabel = this.newLabel.trim()
      if (this.newLabel.length > 0) {
        // 判断该字段是否已经存在
        for (let i of this.labelOptions) {
          if (this.newLabel === i.value) {
            this.$message.info('该标签已存在')
            return
          }
        }
        this.$post('/api/addlabel', { value: this.newLabel, color: '' })
          .then(res => {
            this.dialogVisible = false
            this.labelOptions.push({ l_id: res.lid, value: this.newLabel })
            this.label = this.newLabel
            this.newLabel = ''
            setTimeout(() => this.$message.success('添加成功'), 250)
          })
          .catch(e => {
            this.$message.error('添加失败, ' + e)
          })
      } else {
        this.$message.info('请输入有效的标签名')
      }
    },
    delLabel(lid) {
      this.$post('/api/dellabel', { lid: lid }).then(() => {
        for (var i = 0; i < this.labelOptions.length; ++i) {
          if (this.labelOptions[i].l_id === lid) break
        }
        if (this.label === this.labelOptions[i].value) this.label = ''
        if (i < this.labelOptions.length) this.labelOptions.splice(i, 1)
        this.$message.success('删除成功')
      })
    }
  },
  beforeMount() {
    this.getLabels()
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      vm.$refs.myeditor.initImg() // 清除缓存的图片
      var noteid = vm.$route.params.noteid
      if (noteid) {
        vm.$post('/api/viewnote', { noteid: noteid }).then(res => {
          vm.noteid = res.nid
          vm.title = res.title
          vm.updateContent(res.content)
          vm.label = res.label
          vm.submitState = 'update'
          vm.state = res.state
          vm.ispublic = res.state === 'save'
          vm.updateOld()
        })
      } else {
        vm.resetField()
      }
      // 获取所有的标签
      vm.$post('/api/getlabels').then(res => {
        vm.labelOptions = res.labels
      })
    })
  },
  beforeRouteLeave(to, from, next) {
    // 监听路由退出前
    if (this.checkChange()) {
      var confirmConfig = {
        distinguishCancelAndClose: true,
        confirmButtonText: '好的',
        cancelButtonText: '取消修改'
      }
      this.$confirm(
        '检测到未保存的内容，是否在离开页面前保存修改？',
        '确认信息',
        confirmConfig
      )
        .then(e => e)
        .catch(action => {
          if (action === 'cancel') next()
        })
    } else {
      next()
    }
  }
}
</script>

<style lang="stylus" scoped src="../../assets/css/editor.styl"></style>

<style lang="stylus">
// 修改markdown组件的样式
.editor-cnt-small {
  .v-note-wrapper .v-note-panel, .v-note-wrapper .v-note-op {
    border-left: none;
    border-right: none;
  }
}
</style>
