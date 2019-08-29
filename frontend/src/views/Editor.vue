<template>
  <div class="editor-cnt">
    <div class="editor-title">
      <span>标题&emsp;</span>
      <el-input class="titleinput" v-model="title" placeholder="请输入标题"></el-input>
      <span>&emsp;&emsp;&emsp;&emsp;标签&emsp;</span>
      <el-select v-model="label" placeholder="未分类" @change="handleSelect">
        <el-option v-for="item in labelOptions" :key="item" :label="item" :value="item"></el-option>
        <el-option label="新建标签" value="__new__"></el-option>
      </el-select>
    </div>

    <mavon-editor
      ref="mdeditor"
      v-model="content"
      defaultOpen="edit"
      :boxShadow="false"
      :toolbars="toolbars"
      style="height:600px;"
      @imgAdd="$imgAdd"
    />

    <div class="btn-box">
      <el-button @click="handleSave('temp')">暂存</el-button>
      <el-button @click="handleSave('save')">保存</el-button>
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
import Config from '../assets/js/config'
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
  data() {
    return {
      dialogVisible: false, // 对话框
      noteid: -1,
      title: '',
      label: '',
      content: '',
      labelOptions: ['HTML', 'CSS', 'JS'],
      toolbars: Config.toolbarsConfig,
      newLabel: '',

      submitState: 'new', // new/update 用于判断是更新笔记还是新建笔记
      old_title: '', // 用于缓存比较
      old_label: '', // 用于缓存比较
      old_content: '' // 用于缓存比较
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
      if (this.title.length === 0) {
        this.$message.error('请输入标题')
        return
      }
      this.updateOld()
      var url = this.submitState === 'new' ? '/api/addnote' : '/api/updatenote'
      this.$post(
        url,
        {
          noteid: this.noteid,
          label: this.label,
          title: this.title,
          content: this.content,
          state: state
        },
        () => this.$message.success('保存成功'),
        () => this.$message.error('保存失败')
      )
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
        var subscription = observable.subscribe(observer) // 上传开始
        // subscription.unsubscribe() // 上传取消
      })
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
          confirmButtonText: '保存为草稿',
          cancelButtonText: '取消修改'
        }
      )
        .then(() => {
          this.handleSave('temp')
          this.$message.info('保存成功')
        })
        .catch(action => {
          if (action === 'cancel') {
            next()
          }
        })
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '../assets/default';

.editor-cnt {
  width: default_width;
  margin: 0 auto;
}

.editor-title {
  margin-bottom: 20px;

  .titleinput {
    width: 60%;
  }

  span {
    noselect();
    font-size: 1.125rem;
    color: default_black;
  }
}

.btn-box {
  width: 350px;
  margin: 20px auto;
  display: flex;
  display: -webkit-flex;
  justify-content: space-between;

  .el-button {
    width: 150px;
  }
}
</style>
