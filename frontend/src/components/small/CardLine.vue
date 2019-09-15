<template>
  <div class="card-line">
    <div class="card-label">{{label}}</div>
    <div v-if="value" class="card-value">{{value}}</div>
    <div v-else class="card-value-slot">
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
    width: 36%;
    color: #707377;
    font-size: 1rem;
    font-weight: bold;
    overflow: hidden;
    word-wrap: break-word;
    word-break: break-all;
  }

  .card-value {
    text-align: right;
    color: theme_color;
    font-weight: bold;
    font-size: 1.75rem;
    margin-bottom: 1px;
  }

  .card-value-slot {
    width: 63%;
    text-align: right;
  }
}
</style>
