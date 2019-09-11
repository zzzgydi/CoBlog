// 工具模块

// 格式化时间戳
function parseTime(t) {
  if (typeof t !== 'number') {
    return t
  }
  t = new Date(t)
  var year = t.getFullYear()
  var month = t.getMonth() + 1
  var date = t.getDate()
  var hour = t.getHours()
  var minute = t.getMinutes()
  if (hour < 10) hour = '0' + hour
  if (minute < 10) minute = '0' + minute
  return year + '-' + month + '-' + date + ' ' + hour + ':' + minute
}

// 取两个列表的交集
function arrayIntersection(a, b) {
  var c = a.length <= b.length ? a : b
  var d = a.length > b.length ? a : b
  var e = {}
  var f = []
  for (let i in c) {
    e[c[i].id] = c[i]
  }
  for (let i in d) {
    if (e[d[i].id]) f.push(e[d[i].id])
  }
  return f
}

export default {
  parseTime,
  arrayIntersection
}
