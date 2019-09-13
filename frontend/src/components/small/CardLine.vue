<template>
  <div class="card-line">
    <div class="card-label">{{label}}</div>
    <div v-if="value" class="card-value">{{value}}</div>
    <div v-else>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: ['label', 'value']
}
</script>

<style lang="stylus" scoped>
@import '../../assets/css/default';

.card-line {
  display: flex;
  display: -webkit-flex;
  justify-content: space-between;
  align-items: center;

  .card-label {
    color: #707377;
    font-size: 1rem;
    font-weight: bold;
  }

  .card-value {
    text-align: right;
    color: theme_color;
    font-weight: bold;
    font-size: 1.75rem;
    margin-bottom: 1px;
  }
}
</style>
