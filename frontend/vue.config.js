// 导入compression-webpack-plugin
const CompressionWebpackPlugin = require('compression-webpack-plugin')
// 定义压缩文件类型
const productionGzipExtensions = ['js', 'css']

module.exports = {
  publicPath: '/',
  assetsDir: 'static',
  devServer: {
    host: '0.0.0.0',
    port: 8080,
    proxy: {
      // 配置跨域
      '/api': {
        target: 'http://127.0.0.1:5000/', // 这里后台的地址模拟的;应该填写你们真实的后台接口
        changOrigin: true // 允许跨域
      }
    }
  },
  configureWebpack: {
    plugins: [
      new CompressionWebpackPlugin({
        filename: '[path].gz[query]',
        algorithm: 'gzip',
        test: new RegExp('\\.(' + productionGzipExtensions.join('|') + ')$'),
        threshold: 10240,
        minRatio: 0.8
      })
    ]
  }
}
