<template>
  <div>
    <div v-if="assertSmall">
      <div :class="showBtn?'cata-small':'cata-small cata-small-hide'" @click="clickSmallBtn">
        <i class="el-icon-more"></i>
      </div>
    </div>
    <div v-else class="catalogue-cnt">
      <div class="label-box" v-for="(label, idx) in notes" :key="idx">
        <div class="label">&ensp;{{idx}}</div>
        <div
          class="note-title"
          v-for="note in notes[idx]"
          :key="note.id"
          @click="viewNote(note)"
        >&emsp;&ensp;{{note.title}}</div>
      </div>
    </div>

    <!-- 只有在小屏模式才会打开 -->
    <van-popup v-model="showPopup" position="left" :style="{ height: '100%', width: '60%' }">
      <div class="popup-cnt">
        <div class="pop-logo">
          <span>Co</span>
          <span class="note">Note</span>
        </div>
        <div class="small-box">
          <div class="small-label-box" v-for="(label, idx) in notes" :key="idx">
            <div class="label">{{idx}}</div>
            <div
              class="item-title"
              v-for="note in notes[idx]"
              :key="note.id"
              @click="viewNote(note)"
            >{{note.title}}</div>
          </div>
        </div>
      </div>
    </van-popup>
  </div>
</template>

<script>
// 防抖立即执行
function debounce(func, funcAfter, wait) {
  let timeout
  return function() {
    let context = this
    let args = arguments
    if (timeout) clearTimeout(timeout)
    let callNow = !timeout
    timeout = setTimeout(() => {
      timeout = null
      funcAfter.apply(context, args)
    }, wait)
    if (callNow) func.apply(context, args)
  }
}

export default {
  name: 'catalogue',
  data() {
    return {
      notes: {}, // 标签到笔记数据的映射
      showPopup: false,
      showBtn: true
    }
  },
  computed: {
    assertSmall() {
      return this.$store.state.ssize === 0
    }
  },
  methods: {
    viewNote(note) {
      let path = '/view/' + note.id
      if (this.$route.path !== path) {
        this.showPopup = false
        this.$router.push(path)
      }
    },
    clickSmallBtn() {
      this.showPopup = true
    },
    handleScrollBegin(e) {
      this.showBtn = false
    },
    handleScrollAfter(e) {
      this.showBtn = true
    }
  },
  beforeMount() {
    this.scrollListener = debounce(
      this.handleScrollBegin,
      this.handleScrollAfter,
      300
    )
    window.addEventListener('scroll', this.scrollListener, true) // 监听（绑定）滚轮滚动事件

    // 获取目录
    this.$post('/api/getnotes', {
      state: 'save'
    }).then(res => {
      this.notes = {}
      for (let i in res.notes) {
        let l = res.notes[i].label.trim() || '未分类'
        if (!this.notes[l]) this.notes[l] = []
        res.notes[i].title = res.notes[i].title || '未设置标题'
        this.notes[l].push(res.notes[i])
      }
    })
  }
}
</script>

<style lang="stylus" scoped src="../assets/css/note.styl"></style>
