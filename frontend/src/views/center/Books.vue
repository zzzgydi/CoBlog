<template>
  <div>
    <book :page="countPage"></book>
  </div>
</template>

<script>
import BookCommonVue from '../../components/BookCommon.vue'

var router = {
  books: {
    icon: 'el-icon-notebook-1',
    name: '我的笔记',
    posturl: '/api/usernotes',
    poststate: 'save',
    tagStyle: 'primary'
  },
  private: {
    icon: 'el-icon-lock',
    name: '私人笔记',
    posturl: '/api/usernotes',
    poststate: 'self',
    tagStyle: 'info'
  },
  drafts: {
    icon: 'el-icon-collection',
    name: '草稿箱',
    posturl: '/api/usernotes',
    poststate: 'temp',
    tagStyle: 'warning'
  },
  recycle: {
    icon: 'el-icon-delete',
    name: '回收站',
    posturl: '/api/usernotes',
    poststate: 'del',
    tagStyle: 'danger',
    hideBtn: true
  }
}

export default {
  components: {
    book: BookCommonVue
  },
  data() {
    return {}
  },
  computed: {
    countPage() {
      var id = this.$route.params.id
      if (router[id]) return router[id]
      else this.$router.replace('/404')
      return router.books
    }
  },
  methods: {}
}
</script>
