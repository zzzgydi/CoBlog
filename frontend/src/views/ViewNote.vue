<template>
  <div :class="assertSmallAndMedium?'view-cnt-small':'view-cnt'">
    <div class="view-note">
      <div class="view-head">
        <div class="view-line">
          <el-tag size="mini">{{label}}</el-tag>
          <div v-if="showState">
            <span>&ensp;</span>
            <el-tag size="mini" type="danger">{{stateMsg}}</el-tag>
          </div>
          <div class="view-title">{{title}}</div>
        </div>
        <div class="view-time">
          <span>{{modified}}&emsp;</span>
          <!-- <span class="view-author" @click="switchToPage">
            <i class="el-icon-user"></i>
            {{author}}&ensp;
          </span>-->
          <router-link class="view-author" :to="'/u/' + account">
            <i class="el-icon-user"></i>
            {{author}}&ensp;
          </router-link>
          <span>
            <i class="el-icon-view"></i>
            {{look}}
          </span>
        </div>
      </div>
      <mavon-editor
        v-model="content"
        :boxShadow="false"
        :subfield="false"
        defaultOpen="preview"
        :toolbarsFlag="false"
      />
      <!-- <div class="view-finish">— 完 —</div> -->
    </div>
    <div class="cata-cnt">
      <authorbox
        v-if="!assertSmallAndMedium"
        :account="account"
        :avatar="avatar"
        style="margin-bottom:20px"
      ></authorbox>
      <catalogue ref="catalogue"></catalogue>
    </div>
  </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import CatalogueVue from '../components/Catalogue.vue'
import Tool from '../assets/js/tool'
import AuthorBoxVue from '../components/small/AuthorBox.vue'

var lookTime = {} // 限制频繁的查看笔记刷浏览次数

export default {
  name: 'viewnote',
  components: {
    catalogue: CatalogueVue,
    authorbox: AuthorBoxVue,
    mavonEditor
  },
  data() {
    return {
      account: '',
      author: '未命名',
      avatar: '',
      title: '',
      label: '',
      content: '',
      modified: '',
      look: 0,
      state: 'state',
      loadIns: null
    }
  },
  computed: {
    stateMsg() {
      if (this.state === 'temp') return '草稿'
      else if (this.state === 'del') return '已删除'
      else if (this.state === 'self') return '私密'
      else return ''
    },
    showState() {
      if (this.state === 'save') return false
      return true
    },
    assertSmallAndMedium() {
      return this.$store.state.ssize <= 1
    }
  },
  methods: {
    updateView() {
      this.loadIns = this.$loading({
        background: '#ffffff'
      })
      var noteid = this.$route.params.noteid
      this.lookNote(noteid)
      this.$post('/api/viewnote', { noteid: noteid })
        .then(res => {
          this.account = res.account
          this.avatar = res.avatar
          this.author = res.name || '未命名'
          this.title = res.title || '未设置标题'
          this.label = res.label || '未分类'
          this.content = res.content
          this.modified = Tool.parseTime(res.modified)
          this.state = res.state
          this.look = res.look
          this.loadIns.close()
        })
        .catch(() => {
          this.loadIns.close()
          this.$router.replace('/404')
        })
      this.$refs.catalogue && this.$refs.catalogue.getCatalogue()
    },
    lookNote(noteid) {
      // 观看笔记 - 这里前端做一个判定，1分钟内反复点击是无效的
      var t = new Date().getTime()
      if (lookTime[noteid] && t < lookTime[noteid]) return
      this.$post('/api/looknote', { noteid: noteid }).then(() => {
        lookTime[noteid] = t + 60000
      })
    },
    switchToPage() {
      // 跳转到用户首页
      this.$router.push('/u/' + this.account)
    }
  },
  watch: {
    '$route.params.noteid': function() {
      if (this.$route.path.indexOf('/view/') !== -1) this.updateView()
    }
  },
  beforeMount() {
    this.updateView()
  },
  beforeRouteLeave(to, from, next) {
    this.loadIns.close()
    this.title = ''
    this.label = ''
    this.content = ''
    this.modified = ''
    this.state = ''
    next()
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/note.styl"></style>

<style lang="stylus">
// 修改markdown组件的样式
.view-cnt-small {
  .v-note-wrapper .v-note-panel {
    border-left: none;
    border-right: none;
    border: none;
  }

  .view-note .v-note-wrapper .v-note-panel .v-note-show .v-show-content {
    padding: 5px 15px;
    // background: #f6f6f6;
  }
}

.view-cnt {
  .view-note {
    .v-note-wrapper .v-note-panel .v-note-show .v-show-content {
      background: #fefefe;
    }

    .v-note-wrapper .v-note-panel {
      border: none;
    }
  }
}

// 解析后的md列表没有样式
ul {
  list-style-type: disc;
}
</style>
