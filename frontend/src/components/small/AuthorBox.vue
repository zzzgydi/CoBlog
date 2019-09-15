<template>
  <div class="author-box">
    <div class="top-part">
      <router-link :to="'/u/'+account">
        <img :src="avatar" alt="头像" width="60px" height="60px" />
      </router-link>
      <div class="right-part">
        <router-link class="name" :to="'/u/'+account">{{getName}}</router-link>
        <div class="intro">{{getIntro}}</div>
      </div>
    </div>
    <!-- <div class="bottom-part">{{getIntro}}</div> -->
  </div>
</template>

<script>
export default {
  props: ['account', 'name', 'avatar', 'intro'],
  computed: {
    getIntro() {
      return this.intro || '暂无介绍'
    },
    getName() {
      return this.name || '未命名'
    }
  },
  methods: {
    clickAuthor() {
      this.$router.push('/u/' + this.account)
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '../../assets/css/default';

.author-box {
  padding: 15px;
  background-color: #fff;
  box-shadow: 0 1px 4px 0 rgba(23, 23, 23, 0.1);
  default_radius();

  .top-part {
    display: flex;
    align-items: center;

    .right-part {
      width: calc(100% - 70px);
      margin-left: 10px;

      .name {
        font-size: 1.125rem;
        font-weight: 600;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        color: #303133;
      }

      .intro {
        font-size: 0.875rem;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
      }
    }

    img {
      default_radius();
    }
  }
}
</style>
