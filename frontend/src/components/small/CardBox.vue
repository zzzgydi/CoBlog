<template>
  <div class="card-box">
    <div class="title">{{title}}</div>
    <div class="content-box">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: ['title']
}
</script>

<style lang="stylus" scoped>
@import '../../assets/css/default';

.card-box {
  // padding: 20px 25px;
  box-shadow: 0 1px 4px 0 rgba(0, 0, 0, 0.1);
  background-color: #fefefe;
  default_radius();

  .title {
    padding: 15px 25px;
    color: #909399;
    font-size: 1.125rem;
    border-bottom: 1px solid #e9e9e9;
  }

  .content-box {
    padding: 12px 25px 20px;
  }
}

@media screen and (max-width: mobile_width) {
  .card-box {
    .title {
      padding: 10px 15px;
    }

    .content-box {
      padding: 8px 15px 12px;
    }
  }
}
</style>
