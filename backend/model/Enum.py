# -*- coding=utf-8 -*-

from enum import Enum, IntEnum, unique


@unique
class Status(IntEnum):
    OK          = 0
    LoginReq    = 100   # 需要登录态 但是没有登录
    FormErr     = 101   # 上传数据格式不对
    IdErr       = 102   # id有误
    AcctExist   = 103   # 用户名已经存在
    FileErr     = 104   # 上传文件出错
    AuthErr     = 105   # 权限错误
    ListNull    = 200   # 结果列表为空
    DBErr       = 300   # 数据库操作出现错误
    RegInfoErr  = 301   # 注册用户信息有错
    StatusErr   = 303   # Status参数有误
    UserIDErr   = 304   # UserID不在session里
    Error       = 400
    UnSupport   = 401
    Debug       = 500
    pass