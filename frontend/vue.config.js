module.exports = {
  publicPath: '/',
  assetsDir: 'static',
  devServer: {
    host: '0.0.0.0',
    port: 8080,
    proxy: {
      // 配置跨域
      '/api': {
        target: 'http://localhost:5000/', // 这里后台的地址模拟的;应该填写你们真实的后台接口
        changOrigin: true // 允许跨域
      }
    }
  }
}
