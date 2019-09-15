<template>
  <div class="favorite-cnt">
    <div class="fav-head">
      <div class="fav-head-title" v-show="!assertSmall">
        <i class="el-icon-star-off"></i>
        <span>收藏夹</span>
      </div>
      <div class="fav-head-filter">
        <span>关键词&ensp;</span>
        <el-input class="fav-input" v-model="searchFilter" placeholder="输入关键词" clearable></el-input>
      </div>
    </div>
    <div v-show="isNull && canNullShow">
      <null-view :fav="true"></null-view>
    </div>
    <div v-show="!isNull && canNullShow">
      <div v-for="fav in favurls" :key="fav.fid">
        <fav-box :favurl="fav" @delItem="$delItem"></fav-box>
      </div>
    </div>
  </div>
</template>

<script>
import Tool from '../../assets/js/tool'
import FavoriteBoxVue from '../../components/box/FavoriteBox.vue'
import NullViewVue from '../../components/NullView.vue'

export default {
  components: {
    'fav-box': FavoriteBoxVue,
    'null-view': NullViewVue
  },
  data() {
    return {
      favurls: [],
      searchFilter: '',
      canNullShow: false // 用于第一次进入的时候
    }
  },
  computed: {
    assertSmall() {
      return this.$store.state.ssize === 0
    },
    isNull() {
      return this.favurls.length === 0
    }
  },
  methods: {
    $delItem(fid) {
      var i = 0
      for (; i < this.favurls.length; ++i) {
        if (this.favurls[i].fid === fid) break
      }
      if (i < this.favurls.length) this.favurls.splice(i, 1)
    }
  },
  beforeMount() {
    this.$post('/api/allurls')
      .then(res => {
        for (let i = 0; i < res.lists.length; ++i) {
          res.lists[i].modified = Tool.parseTime(res.lists[i].modified)
        }
        this.favurls = res.lists
        this.canNullShow = true
      })
      .catch(() => (this.canNullShow = true))
  }
}
</script>

<style lang="stylus" scoped src="../../assets/css/favorite.styl"></style>
