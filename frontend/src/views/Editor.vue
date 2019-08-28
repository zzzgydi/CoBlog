<template>
  <div class="editor-cnt">
    <div class="editor-title">
      <span>标题&emsp;</span>
      <el-input class="titleinput" v-model="title" placeholder="请输入标题"></el-input>
      <span>&emsp;&emsp;&emsp;&emsp;标签&emsp;</span>
      <el-select v-model="label" placeholder="未分类">
        <el-option v-for="item in labelOptions" :key="item" :label="item" :value="item"></el-option>
      </el-select>
    </div>

    <mavon-editor v-model="content" defaultOpen="edit" :toolbars="toolbars" style="height:600px;" />

    <div>
      <el-button>暂存</el-button>
      <el-button @click="handleSave">保存</el-button>
    </div>
  </div>
</template>

<script>
var toolbarsConfig = {
  bold: true, // 粗体
  italic: true, // 斜体
  header: true, // 标题
  underline: true, // 下划线
  strikethrough: true, // 中划线
  mark: true, // 标记
  superscript: true, // 上角标
  subscript: true, // 下角标
  quote: true, // 引用
  ol: true, // 有序列表
  ul: true, // 无序列表
  link: true, // 链接
  imagelink: true, // 图片链接
  code: true, // code
  table: true, // 表格
  fullscreen: true, // 全屏编辑
  readmodel: false, // 沉浸式阅读
  htmlcode: true, // 展示html源码
  help: false, // 帮助
  undo: true, // 上一步
  redo: true, // 下一步
  trash: true, // 清空
  save: true, // 保存（触发events中的save事件）
  navigation: true, // 导航目录
  alignleft: true, // 左对齐
  aligncenter: true, // 居中
  alignright: true, // 右对齐
  subfield: false, // 单双栏模式
  preview: true // 预览
}
export default {
  data() {
    return {
      title: '',
      label: '',
      content: '',
      labelOptions: ['HTML', 'CSS', 'JS'],
      toolbars: toolbarsConfig
    }
  },
  methods: {
    handleSave() {
      this.$post(
        '/api/addnote',
        {
          label: this.label,
          title: this.title,
          content: this.content,
          state: 'save'
        },
        res => {
          console.log(res)
        }
      )
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '../assets/default';

.editor-cnt {
  width: 1100px;
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
</style>