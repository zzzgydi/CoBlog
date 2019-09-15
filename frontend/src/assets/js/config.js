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
  save: false, // 保存（触发events中的save事件）
  navigation: true, // 导航目录
  alignleft: true, // 左对齐
  aligncenter: true, // 居中
  alignright: true, // 右对齐
  subfield: false, // 单双栏模式
  preview: true // 预览
}

// 中等宽度的配置
var toolbarsConfigMedium = {
  bold: false, // 粗体
  italic: false, // 斜体
  header: false, // 标题
  underline: true, // 下划线
  strikethrough: true, // 中划线
  mark: false, // 标记
  superscript: true, // 上角标
  subscript: true, // 下角标
  quote: true, // 引用
  ol: false, // 有序列表
  ul: false, // 无序列表
  link: true, // 链接
  imagelink: true, // 图片链接
  code: true, // code
  table: true, // 表格
  fullscreen: true, // 全屏编辑
  readmodel: false, // 沉浸式阅读
  htmlcode: false, // 展示html源码
  help: false, // 帮助
  undo: true, // 上一步
  redo: true, // 下一步
  trash: false, // 清空
  save: false, // 保存（触发events中的save事件）
  navigation: true, // 导航目录
  alignleft: true, // 左对齐
  aligncenter: true, // 居中
  alignright: true, // 右对齐
  subfield: false, // 单双栏模式
  preview: true // 预览
}

// 最小宽度的配置
var toolbarsConfigSmall = {
  bold: false, // 粗体
  italic: false, // 斜体
  header: false, // 标题
  underline: false, // 下划线
  strikethrough: false, // 中划线
  mark: true, // 标记
  superscript: true, // 上角标
  subscript: true, // 下角标
  quote: false, // 引用
  ol: false, // 有序列表
  ul: false, // 无序列表
  link: false, // 链接
  imagelink: true, // 图片链接
  code: false, // code
  table: true, // 表格
  fullscreen: true, // 全屏编辑
  readmodel: false, // 沉浸式阅读
  htmlcode: false, // 展示html源码
  help: false, // 帮助
  undo: true, // 上一步
  redo: true, // 下一步
  trash: false, // 清空
  save: false, // 保存（触发events中的save事件）
  navigation: false, // 导航目录
  alignleft: false, // 左对齐
  aligncenter: false, // 居中
  alignright: false, // 右对齐
  subfield: false, // 单双栏模式
  preview: false // 预览
}

// 页面导航对象
const navObj = {
  mobileHome: {
    url: '/',
    name: '首 页',
    icon: 'el-icon-house'
  },
  home: {
    url: '/',
    name: 'Home',
    icon: 'el-icon-house'
  },
  login: {
    url: '/login',
    name: 'Login',
    icon: 'el-icon-lock'
  },
  editor: {
    url: '/center/edit',
    name: '编辑笔记',
    icon: 'el-icon-edit'
  },
  books: {
    url: '/center/note/books',
    name: '我的笔记',
    icon: 'el-icon-notebook-1'
  },
  // private: {
  //   url: '/center/note/private',
  //   name: '私人笔记',
  //   icon: 'el-icon-lock'
  // },
  favorite: {
    url: '/center/favorite',
    name: '收藏夹',
    icon: 'el-icon-star-off'
  },
  editfav: {
    url: '/center/editfav',
    name: '添加收藏',
    icon: 'el-icon-edit-outline'
  },
  center: {
    url: '/center',
    name: 'Menu',
    icon: 'el-icon-user-solid'
  },
  setting: {
    url: '/center/setting',
    name: '个人设置',
    icon: 'el-icon-setting'
  },
  drafts: {
    url: '/center/note/drafts',
    name: '草稿箱',
    icon: 'el-icon-collection'
  },
  recycle: {
    url: '/center/note/recycle',
    name: '回收站',
    icon: 'el-icon-delete'
  },
  logout: {
    url: 'logout',
    name: '退出登录',
    icon: 'el-icon-switch-button'
  },
  userpage: {
    url: 'page',
    name: '个人主页',
    icon: 'el-icon-cpu'
  }
}

// 个人中心页
var centerPaths = [
  navObj.editor,
  navObj.editfav,
  navObj.books,
  // navObj.private,
  navObj.favorite,
  navObj.drafts,
  navObj.recycle,
  navObj.userpage,
  navObj.setting,
  navObj.logout
]

// 用于导航栏在移动端模式下
var mobilePaths = [
  navObj.mobileHome,
  navObj.editor,
  navObj.editfav,
  navObj.books,
  // navObj.private,
  navObj.favorite,
  navObj.drafts,
  navObj.recycle,
  navObj.userpage,
  navObj.setting,
  navObj.logout
]

// 路由到页面名称的映射
var pageTitleMap = {
  // '/': 'HOME',
  '/center/edit': '编辑笔记',
  '/center/note/books': '我的笔记',
  // '/center/note/private': '私人笔记',
  '/center/note/drafts': '草稿箱',
  '/center/note/recycle': '回收站',
  '/center/setting': '个人设置',
  '/center/favorite': '收藏夹',
  '/center/editfav': '添加收藏'
}

export default {
  toolbarsConfig,
  toolbarsConfigMedium,
  toolbarsConfigSmall,
  centerPaths,
  mobilePaths,
  pageTitleMap,
  navObj
}
