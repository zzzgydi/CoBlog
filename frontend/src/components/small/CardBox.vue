<template>
  <div class="card-box">
    <div class="title">{{title}}</div>
    <slot></slot>
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
  padding: 20px 25px;
  box-shadow: 0 1px 4px 0 rgba(0, 0, 0, 0.1);
  background-color: #fefefe;
  border-radius(6px);

  .title {
    color: #909399;
    font-size: 1.125rem;
    padding-bottom: 10px;
    border-bottom: 1px solid #e6e6e6;
    margin-bottom: 10px;
  }
}

@media screen and (max-width: mobile_width) {
  .card-box {
    padding: 12px 15px;
  }
}
</style>
