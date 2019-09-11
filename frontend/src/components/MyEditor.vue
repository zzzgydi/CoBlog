<template>
  <div>
    <!-- 打包一下md编辑器 -->
    <mavon-editor
      ref="editor"
      v-model="mycontent"
      defaultOpen="edit"
      :boxShadow="false"
      :toolbars="toolbars"
      :autofocus="false"
      :style="'height:'+ editorHeight"
      @change="$change"
      @imgAdd="$imgAdd"
      @imgDel="$imgDel"
      @fullScreen="$fullScreen"
      @save="$saveToTemp"
    />
  </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import Config from '../assets/js/config'
import qiniu from '../assets/js/qiniu'

export default {
  components: {
    mavonEditor
  },
  props: {
    cnt: String
  },
  model: {
    prop: 'cnt',
    event: 'returnBack'
  },
  computed: {
    toolbars() {
      switch (this.$store.state.ssize) {
        case 0:
          return Config.toolbarsConfigSmall
        case 1:
          return Config.toolbarsConfigMedium
      }
      return Config.toolbarsConfig
    }
  },
  data() {
    this.imgs = {}
    return {
      mycontent: this.cnt,
      editorHeight: '600px',
      targetNum: 0, // 用来设置目标上传任务的个数
      finishNum: 0, // 用来设置已经完成的任务个数
      errorNum: 0 // 用来记录有几个文件上传失败
    }
  },
  watch: {
    finishNum(newVal, oldVal) {
      if (newVal && newVal === this.targetNum) {
        this.$emit('finishUpload', this.errorNum) // 触发全部完成事件
      }
    }
  },
  methods: {
    $change(val) {
      // 实现v-model
      this.$emit('returnBack', val)
    },
    $imgAdd(pos, file) {
      this.imgs[pos] = file
    },
    $imgDel(filename) {
      this.imgs[filename] = null
    },
    $fullScreen(e) {
      if (e) {
        this.editorHeight = window.innerHeight + 'px'
      } else {
        this.editorHeight = '600px'
      }
    },
    $saveToTemp() {
      this.$emit('ctrls') // 触发父组件保存
    },
    uploadAllImgs(resolve) {
      // 由父组件触发，触发将保存所有图片
      var totalSize = 0 // 计算总的大小
      var loadSize = 0 // 已上传大小
      this.targetNum = 0
      this.finishNum = 0
      this.errorNum = 0
      for (let pos in this.imgs) {
        let file = this.imgs[pos]
        if (!file) continue
        totalSize += file.size
        this.targetNum += 1 // 记录文件个数
      }
      if (totalSize === 0) return // 无图片

      for (let pos in this.imgs) {
        let file = this.imgs[pos]
        if (!file) continue
        let filename = file.name
        this.$post('/api/gettoken', {
          filename: filename
        }).then(res => {
          qiniu
            .qiniuUpload(file, filename, res.key, res.token, function(res) {
              // let loaded = loadSize + (res.total.percent * file.size) / 100 // 按百分比
              // resolve({ progress: Math.ceil((loaded / totalSize) * 100) })
              // 这里的响应里的大小和前面获得的文件大小值有出入，所以这里用百分比算
            })
            .then(res => {
              let url = 'http://oss.segydi.cn/' + res.key
              this.$refs.editor.$img2Url(pos, url)
              loadSize += file.size
              this.imgs[pos] = null // 删除已经上传的文件
              this.finishNum += 1
              resolve({ progress: Math.ceil((loadSize / totalSize) * 100) })
            })
            .catch(err => {
              console.log('img upload error:', file.name, err)
              this.$message.error('图片上传有误')
              this.finishNum += 1
              this.errorNum += 1
            })
        })
      }
    },
    checkImg() {
      // 检查是否有图片需要上传
      for (let pos in this.imgs) {
        if (this.imgs[pos]) return true
      }
      return false
    },
    initImg() {
      // 初始化图片数组
      this.$refs.editor.$refs.toolbar_left.img_file.splice(1)
      this.imgs = {}
    }
  }
}
</script>

<style lang="stylus" scoped></style>
