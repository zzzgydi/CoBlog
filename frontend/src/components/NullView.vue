<template>
  <div class="null-box">
    <div class="null-head">
      <span>Empty List</span>
    </div>
    <div class="go-link" @click="gotoEdit">
      <span>make note&ensp;</span>
      <i class="el-icon-right"></i>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    gotoEdit() {
      this.$router.push('/center/edit')
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '../assets/css/default';

.null-box {
  // background-color: #fefefe;
  text-align: center;
  padding: 60px 0;

  .null-head {
    // font-size: 45px;
    text-shadow: 1px 2px 2px rgba(0, 0, 0, 0.32);
    // color: #6a67ce;
    letter-spacing: 1px;
    text-transform: uppercase;
    font-weight: bold;
    color: #909399;
  }

  .go-link {
    noselect();
    margin-top: 50px;
    cursor: pointer;
    font-size: 1rem;
    text-transform: uppercase;
    color: #fff;
    padding: 14px 30px;
    // letter-spacing: 1px;
    display: inline-block;
    // border-top: 2px solid #FFF;
    background: theme_color_a(0.8);
    transition(0.5s);
    border-radius(30px);
    -webkit-box-shadow: -1px 5px 18px -6px rgba(0, 0, 0, 0.75);
    -moz-box-shadow: -1px 5px 18px -6px rgba(0, 0, 0, 0.75);
    box-shadow: -1px 5px 18px -6px rgba(0, 0, 0, 0.75);

    &:hover {
      background: #909399; // #e3aa01;
    }
  }
}

@media screen and (max-width: mobile_width) {
  .null-head {
    font-size: 2rem;
  }
}

@media screen and (min-width: mobile_width) {
  .null-head {
    font-size: 45px;
  }
}
</style>
