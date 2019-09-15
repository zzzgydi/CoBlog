<template>
  <div class="userpage-cnt">
    <div :class="assertSmall ? 'head-box-small' : 'head-box'">
      <img id="backimg" :src="backimg" width="100%" />
      <div class="img-box">
        <img id="avatar" :src="avatar" alt="这是头像" />
      </div>
      <div class="text-box">
        <h2 class="name">{{name}}</h2>
        <p>这里应该有一个介绍</p>
      </div>
    </div>
    <div v-for="note in notes" :key="note.id">
      <note-box :note="note"></note-box>
    </div>
  </div>
</template>

<script>
import Api from '../../plugins/api'
import Tool from '../../assets/js/tool'
import NoteBoxVue from '../../components/box/NoteBox3.vue'

export default {
  components: {
    'note-box': NoteBoxVue
  },
  data() {
    return {
      name: '',
      avatar: '',
      backimg: '',
      flag: 0,
      alias: '',
      notes: []
    }
  },
  computed: {
    assertSmall() {
      return this.$store.state.ssize === 0
    }
  },
  methods: {
    getPageInfo(account) {
      this.$post('/api/page/info', { user: account }).then(res => {
        console.log(res)
      })
    },
    getPageNotes(account) {
      this.$post('/api/page/notes', { user: account }).then(res => {
        for (let i in res.notes) {
          res.notes[i].modified = Tool.parseTime(res.notes[i].modified)
          res.notes[i].label = res.notes[i].label.trim() || '未分类'
          res.notes[i].title = res.notes[i].title || '未设置标题'
          res.notes[i].author = res.notes[i].name || '未命名'
        }
        this.notes = res.notes
      })
    }
  },
  beforeMount() {
    let account = this.$route.params.user
    this.getPageNotes(account)
  },
  beforeRouteEnter(to, from, next) {
    // 判断是否需要跳转
    let account = to.params.user
    Api.post('/api/page/info', { user: account })
      .then(res => {
        if (res.flag === 1 && Tool.checkUrl(res.alias)) {
          window.location.replace(res.alias)
        } else {
          next(vm => {
            // 其他情况则选择展示默认的主页
            vm.name = res.name || '未命名'
            vm.avatar = res.avatar
            vm.backimg =
              res.backimg || 'http://oss.segydi.cn/default-background.jpg'
            vm.flag = res.flag
            vm.alias = res.alias
          })
        }
      })
      .catch(() => {
        // 用户不存在，或者别的什么错误
        // next('/404')
        window.location.replace('/404')
      })
  }
}
</script>

<style lang="stylus" scoped src="../../assets/css/userpage.styl"></style>
