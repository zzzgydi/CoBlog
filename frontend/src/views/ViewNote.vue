<template>
  <div class="viewnote-cnt">
    <div style="width:20%;margin-top:20px">
      <catalogue></catalogue>
    </div>

    <div class="viewnote">
      <div class="view-head">
        <el-tag>{{label}}</el-tag>
        <div v-if="showState">
          &ensp;
          <el-tag type="danger">{{stateMsg}}</el-tag>
        </div>

        <div class="view-title">{{title}}</div>
      </div>
      <mavon-editor
        v-model="content"
        :boxShadow="false"
        :subfield="false"
        defaultOpen="preview"
        :toolbarsFlag="false"
      />
      <div>{{modified}}</div>
    </div>
  </div>
</template>

<script>
import CatalogueVue from '../components/Catalogue.vue'
import Tool from '../assets/js/tool'

export default {
  name: 'viewnote',
  components: {
    catalogue: CatalogueVue
  },
  data() {
    return {
      title: '',
      label: '',
      content: '',
      modified: '',
      state: ''
    }
  },
  computed: {
    stateMsg() {
      if (this.state === 'temp') return '草稿'
      else return '已删除'
    },
    showState() {
      if (this.state === 'temp' || this.state === 'del') return true
      return false
    }
  },
  methods: {
    updateView() {
      var noteid = this.$route.params.noteid
      this.$post('/api/viewnote', { noteid: noteid })
        .then(res => {
          this.title = res.title || '未设置标题'
          this.label = res.label || '未分类'
          this.content = res.content
          this.modified = Tool.parseTime(res.modified)
          this.state = res.state
        })
        .catch(() => {
          this.$router.replace('/404')
        })
    }
  },
  watch: {
    '$route.params.noteid': function() {
      if (this.$route.path.indexOf('/view') !== -1) this.updateView()
    }
  },
  beforeMount() {
    this.updateView()
  },
  beforeRouteLeave(to, from, next) {
    // ...
    this.title = ''
    this.label = ''
    this.content = ''
    this.modified = ''
    this.state = ''
    next()
  }
}
</script>

<style lang="stylus" scoped>
@import '../assets/default';

.viewnote-cnt {
  max-width: 1300px;
  min-width: 1000px;
  display: flex;
  display: -webkit-flex;
  justify-content: space-between;
  margin: 0 auto;
}

.viewnote {
  width: 75%;
}

.view-head {
  display: flex;
  display: -webkit-flex;
  align-items: center;

  .view-title {
    font-size: 2rem;
    line-height: 60px;
    margin-left: 1rem;
  }
}
</style>
