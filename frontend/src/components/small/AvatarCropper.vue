<template>
  <div class="avatar-cropper">
    <div class="avatar-cropper-overlay" v-if="dataUrl">
      <div class="avatar-cropper-mark">
        <a @click="destroy" class="avatar-cropper-close" href="javascript:;">
          <i class="el-icon-close"></i>
        </a>
      </div>
      <div class="avatar-cropper-container">
        <div class="avatar-cropper-image-container">
          <img :src="dataUrl" @load.stop="createCropper" alt ref="img" />
        </div>
        <div class="avatar-cropper-footer">
          <button @click.stop.prevent="destroy" class="avatar-cropper-btn cancel-btn">取消</button>
          <button @click.stop.prevent="submit" class="avatar-cropper-btn submit-btn">提交</button>
        </div>
      </div>
    </div>
    <input :accept="mimes" style="display:none;" ref="input" type="file" />
  </div>
</template>

<script>
import 'cropperjs/dist/cropper.css'
import Cropper from 'cropperjs'
import qiniu from '../../assets/js/qiniu'

export default {
  props: {
    cropperOptions: {
      type: Object,
      default() {
        return {
          aspectRatio: 1,
          autoCropArea: 1,
          viewMode: 1,
          movable: false,
          zoomable: false
        }
      }
    },
    outputOptions: {
      type: Object
    },
    outputMime: {
      type: String,
      default: null
    },
    outputQuality: {
      type: Number,
      default: 0.9
    },
    mimes: {
      type: String,
      default: 'image/*'
    }
  },
  data() {
    return {
      cropper: undefined,
      dataUrl: undefined,
      filename: undefined
    }
  },
  methods: {
    destroy() {
      this.cropper.destroy()
      this.$refs.input.value = ''
      this.dataUrl = undefined
    },
    submit() {
      this.uploadImage()
      this.destroy()
    },
    pickImage() {
      this.$refs.input.click()
    },
    createCropper() {
      this.cropper = new Cropper(this.$refs.img, this.cropperOptions)
    },
    uploadImage() {
      let filename = this.filename
      this.cropper.getCroppedCanvas(this.outputOptions).toBlob(
        blob => {
          this.$post('/api/avatartoken', {
            filename: filename
          }).then(res => {
            qiniu
              .qiniuUpload(blob, filename, res.key, res.token)
              .then(res => {
                let url = 'http://oss.segydi.cn/' + res.key // 获得了新头像地址
                this.$message.success('上传成功')
                console.log(url)
                this.$store.commit('setAvatar', url) // 更新头像
              })
              .catch(err => {
                console.log('img upload error:', filename, err)
                this.$message.error('图片上传有误')
              })
          })
        },
        this.outputMime,
        this.outputQuality
      )
    }
  },
  mounted() {
    // listen for input file changes
    let fileInput = this.$refs.input
    fileInput.addEventListener('change', () => {
      if (fileInput.files != null && fileInput.files[0] != null) {
        let reader = new FileReader()
        reader.onload = e => {
          this.dataUrl = e.target.result
        }

        reader.readAsDataURL(fileInput.files[0])

        this.filename = fileInput.files[0].name || 'unknown'
        this.mimeType = this.mimeType || fileInput.files[0].type
        this.$emit('changed', fileInput.files[0], reader)
      }
    })
  }
}
</script>

<style lang="stylus" scoped>
@import '../../assets/css/default';

.avatar-cropper {
  .avatar-cropper-overlay {
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 99999;
  }

  .avatar-cropper-close {
    float: right;
    padding: 20px;
    font-size: 3rem;
    color: #fff;
    font-weight: 100;
    text-shadow: 0px 1px rgba(40, 40, 40, 0.3);
  }

  .avatar-cropper-mark {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.3);
  }

  .avatar-cropper-container {
    background: #fff;
    z-index: 999;
    box-shadow: 1px 1px 5px rgba(100, 100, 100, 0.14);
    // padding: 2px;
    border-radius(6px);

    .avatar-cropper-image-container {
      position: relative;
      max-width: 400px;
      height: 300px;
    }

    img {
      max-width: 100%;
      height: 100%;
    }

    .avatar-cropper-footer {
      display: flex;
      align-items: stretch;
      align-content: stretch;
      justify-content: space-between;

      .avatar-cropper-btn {
        width: 50%;
        padding: 15px 0;
        cursor: pointer;
        border: none;
        background: transparent;
        outline: none;
      }

      .cancel-btn {
        color: #F56C6C;
        border-bottom-left-radius: 6px;

        &:hover {
          background-color: #F56C6C;
          color: #fff;
        }
      }

      .submit-btn {
        color: theme_color;
        border-bottom-right-radius: 6px;

        &:hover {
          background-color: theme_color;
          color: #fff;
        }
      }
    }
  }
}
</style>
