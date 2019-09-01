<template>
  <div class="error-cnt">
    <h1>
      Random
      <br v-if="assertSmall" />
      <span>Error</span> Page
    </h1>
    <div class="layout">
      <h2>404</h2>
      <h3>
        Oops!
        <br v-if="assertSmall" />Page Not Found
      </h3>
    </div>
    <div class="back-link" @click="ClickBack">
      <i class="el-icon-back"></i>
      Go back&ensp;
    </div>
  </div>
</template>

<script>
export default {
  name: 'error',
  computed: {
    assertSmall() {
      return this.$store.state.ssize === 0
    }
  },
  methods: {
    ClickBack() {
      this.$router.go(-1)
    }
  }
}
</script>
<style lang="stylus" scoped>
@import '../assets/css/default';

.error-cnt {
  margin: 66px 0;
  text-align: center;
  color: #909399;
  noselect();
}

.layout {
  margin-top: 50px;
}

.back-link {
  margin-top: 2rem;
  cursor: pointer;
  font-size: 1em;
  text-transform: uppercase;
  color: #fff;
  padding: 0.8em 2em;
  letter-spacing: 1px;
  display: inline-block;
  background: theme_color;
  transition(0.5s);
  border-radius(30px);
  -webkit-box-shadow: -1px 10px 18px -6px rgba(0, 0, 0, 0.75);
  -moz-box-shadow: -1px 10px 18px -6px rgba(0, 0, 0, 0.75);
  box-shadow: -1px 10px 18px -6px rgba(0, 0, 0, 0.75);

  &:hover {
    background: #909399; // #e3aa01;
  }
}

@media screen and (max-width: mobile_width) {
  h2 {
    font-size: 6rem;
  }

  h3 {
    font-size: 2rem;
  }
}

@media screen and (min-width: mobile_width) {
  h1 {
    font-size: 45px;
  }

  h2 {
    font-size: 8rem;
  }

  h3 {
    font-size: 50px;
  }
}

h1 {
  // color: #6a67ce;
  letter-spacing: 0px;
  text-transform: uppercase;
}

h2 {
  font-weight: bold;
  text-transform: uppercase;
  text-shadow: 2px 2px 2px rgba(16, 16, 16, 0.8);
  color: #909399;
}

span {
  // font-weight: 700;
  color: theme_color;
}

h3 {
  text-transform: capitalize;
  font-weight: 500;
  color: #909399;
}
</style>
