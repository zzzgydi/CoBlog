<template>
  <div class="avatar-cnt">
    <div class="avatar-img">
      <img :src="avatarUrl" alt="头像" width="60px" />
    </div>
    <div class="hover-btn">
      <el-button
        class="cropper-btn"
        type="primary"
        plain
        @click="handleClick"
        circle
        size="small"
        icon="el-icon-edit"
      ></el-button>
    </div>
    <avatar-cropper ref="cropper"></avatar-cropper>
  </div>
</template>

<script>
import AvatarCropperVue from '../../components/small/AvatarCropper.vue'

export default {
  components: {
    'avatar-cropper': AvatarCropperVue
  },
  computed: {
    avatarUrl() {
      return this.$store.state.avatar
    }
  },
  methods: {
    handleClick() {
      this.$refs.cropper.pickImage()
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '../../assets/css/default';

img_width = 60px;

.avatar-cnt {
  width: img_width;
  height: img_width;
  position: relative;
  border: 1px solid rgb(195, 194, 235);
  border-radius(8px);

  .avatar-img {
    width: img_width;
    height: img_width;
    border-radius(8px);
    overflow: hidden;

    img {
      border-radius(8px);
    }
  }

  .hover-btn {
    position: absolute;
    top: ((img_width - 32) / 2)px;
    left: -20px;
  }
}
</style>
