<template>
  <div class="editor-cnt">
    <div class="editor-head">
      <div class="editor-title">
        <span>标题&ensp;</span>
        <el-input class="title-input" v-model="title" placeholder="请输入标题"></el-input>
      </div>
      <div class="editor-select">
        <span>标签&ensp;</span>
        <el-select v-model="label" placeholder="未分类" @change="handleSelect">
          <el-option v-for="item in labelOptions" :key="item" :label="item" :value="item"></el-option>
          <el-option label="新建标签" value="__new__"></el-option>
        </el-select>
      </div>
    </div>

    <div :class="assertSmall?'editor-cnt-small':''">
      <mavon-editor
        ref="mdeditor"
        v-model="content"
        defaultOpen="edit"
        :boxShadow="false"
        :toolbars="toolbars"
        :style="'height:'+ editorHeight"
        @imgAdd="$imgAdd"
        @fullScreen="$fullScreen"
      />
    </div>
    <div class="btn-box" v-if="!assertSmall">
      <el-button type="danger" plain @click="handleSave('self')">私人笔记</el-button>
      <el-button type="info" plain @click="handleSave('temp')">草稿笔记</el-button>
      <el-button type="primary" plain @click="handleSave('save')">发布</el-button>
    </div>

    <div class="btn-box-small" v-else>
      <el-button size="small" type="danger" plain @click="handleSave('self')">私人笔记</el-button>
      <el-button size="small" type="info" plain @click="handleSave('temp')">草稿笔记</el-button>
      <el-button size="small" type="primary" plain @click="handleSave('save')">发布</el-button>
    </div>

    <el-dialog title="新增标签" width="360px" :visible.sync="dialogVisible" @close="dialogClose">
      <el-input v-model="newLabel" clearable placeholder="请输入标签名称"></el-input>
      <div style="margin-top:20px;text-align:center;">
        <el-button type="success" plain @click="addLabel" style="width:120px;">新增</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import Config from '../../assets/js/config'
import * as qiniu from 'qiniu-js'

// 七牛云的参数配置
var putExtra = {
  // 需要设置fname属性
  fname: '',
  params: {},
  mimeType: ['image/png', 'image/jpeg', 'image/gif']
}
var config = {
  useCdnDomain: false,
  region: qiniu.region.z2
}
function getObserver(vm, pos) {
  // 获取一个观察者对象
  return {
    next(res) {
      // console.log(res)
    },
    error(err) {
      if (!vm) {
        console.log('上传失败:', err)
      } else {
        vm.$message.error('图片上传失败')
      }
    },
    complete(res) {
      if (!vm) {
        console.log('上传环境异常')
        return
      }
      var url = 'http://oss.segydi.cn/' + res.key
      vm.$refs.mdeditor.$img2Url(pos, url)
    }
  }
}

export default {
  name: 'editor',
  components: {
    mavonEditor
  },
  data() {
    return {
      dialogVisible: false, // 对话框
      noteid: -1,
      title: '',
      label: '',
      content: '',
      labelOptions: ['HTML', 'CSS', 'JS'],
      newLabel: '',

      submitState: 'new', // new/update 用于判断是更新笔记还是新建笔记
      old_title: '', // 用于缓存比较
      old_label: '', // 用于缓存比较
      old_content: '', // 用于缓存比较

      editorHeight: '600px'
    }
  },
  computed: {
    assertSmall() {
      return this.$store.state.ssize === 0
    },
    toolbars() {
      switch (this.$store.state.ssize) {
        case 0:
          return Config.toolbarsConfigSmall
        case 1:
          return Config.toolbarsConfigMedium
        case 2:
          return Config.toolbarsConfig
        default:
          return Config.toolbarsConfig
      }
    }
  },
  methods: {
    resetField() {
      this.noteid = -1
      this.title = ''
      this.label = ''
      this.content = ''
      this.submitState = 'new'
      this.updateOld()
    },
    updateOld() {
      this.old_title = this.title
      this.old_label = this.label
      this.old_content = this.content
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
      var msg = ''
      switch (state) {
        case 'save':
          if (this.submitState === 'new') msg = '是否确认发布新笔记？'
          else msg = '是否确认修改笔记？'
          break
        case 'self':
          msg = '是否提交为私人笔记？'
          break
        case 'temp':
          msg = '是否提交到草稿箱？'
          break
      }
      var url = this.submitState === 'new' ? '/api/addnote' : '/api/updatenote'
      this.$confirm(msg, '提示')
        .then(() => {
          this.$post(url, {
            noteid: this.noteid,
            label: this.label,
            title: this.title,
            content: this.content,
            state: state
          })
            .then(() => {
              this.resetField()
              this.$message.success('保存成功')
            })
            .catch(e => {
              this.$message.error('保存失败')
            })
        })
        .catch(err => err)
    },
    $imgAdd(pos, file) {
      // 获取token
      this.$post('/api/gettoken', {
        filename: file.name
      }).then(res => {
        putExtra.fname = file.name
        var observable = qiniu.upload(
          file,
          res.key,
          res.token,
          putExtra,
          config
        )
        var observer = getObserver(this, pos)
        observable.subscribe(observer) // 上传开始
        // var subscription = observable.subscribe(observer) // 上传开始
        // subscription.unsubscribe() // 上传取消
      })
    },
    $fullScreen(e) {
      if (e) {
        this.editorHeight = window.innerHeight + 'px'
      } else {
        this.editorHeight = '600px'
      }
    },
    handleSelect(value) {
      if (value === '__new__') {
        this.dialogVisible = true
      }
    },
    dialogClose() {
      if (this.label === '__new__') {
        this.label = ''
      }
    },
    addLabel() {
      if (this.newLabel.length > 0) {
        this.$post('/api/addlabel', { value: this.newLabel, color: '' }).then(
          res => {
            this.$message.success('添加成功')
            this.labelOptions.push(this.newLabel)
            this.label = this.newLabel
            this.newLabel = ''
            this.dialogVisible = false
          }
        )
      }
    }
  },
  beforeMount() {
    // 获取所有的标签
    this.$post('/api/getlabels').then(res => {
      this.labelOptions = res.labels
    })
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      var noteid = vm.$route.params.noteid
      if (noteid) {
        vm.$post('/api/viewnote', { noteid: noteid }).then(res => {
          vm.noteid = res.id
          vm.title = res.title
          vm.content = res.content
          vm.label = res.label
          vm.submitState = 'update'
          vm.updateOld()
        })
      } else {
        vm.resetField()
      }
    })
  },
  beforeRouteLeave(to, from, next) {
    if (
      this.old_title === this.title &&
      this.old_label === this.label &&
      this.old_content === this.content
    ) {
      next()
    } else {
      this.$confirm(
        '检测到未保存的内容，是否在离开页面前保存修改？',
        '确认信息',
        {
          distinguishCancelAndClose: true,
          confirmButtonText: '好的',
          cancelButtonText: '取消修改'
        }
      )
        .then(e => e)
        .catch(action => {
          if (action === 'cancel') {
            next()
          }
        })
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
