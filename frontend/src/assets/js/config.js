// 编辑器页面的编辑器配置
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

// 登陆后的导航栏配置
var navListLogin = [
  {
    url: '/edit',
    name: '添加笔记'
  },
  {
    url: '/books',
    name: '我的笔记'
  },
  {
    url: '/drafts',
    name: '草稿箱'
  },
  {
    url: '/recycle',
    name: '回收站'
  },
  {
    url: '/center',
    name: '个人中心'
  }
]

// 未登录的导航栏配置
var navListNotLogin = [
  {
    url: '/register',
    name: '注册'
  },
  {
    url: '/login',
    name: '登录'
  }
]

// 个人中心页
var centerPaths = [
  {
    url: '/center/edit',
    name: '添加笔记',
    icon: 'el-icon-edit'
  },
  {
    url: '/center/books',
    name: '我的笔记',
    icon: 'el-icon-notebook-1'
  },
  {
    url: '/center/drafts',
    name: '草稿箱',
    icon: 'el-icon-collection'
  },
  {
    url: '/center/recycle',
    name: '回收站',
    icon: 'el-icon-delete'
  }
]

export default {
  toolbarsConfig,
  navListLogin,
  navListNotLogin,
  centerPaths
}
