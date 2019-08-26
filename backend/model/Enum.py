# -*- coding=utf-8 -*-

from enum import Enum, IntEnum, unique


@unique
class Status(IntEnum):
    OK          = 0
    LoginErr    = 100   # 登录有误
    FormErr     = 101   # 上传数据格式不对
    IdErr       = 102   # id有误
    AcctExist   = 103   # 用户名已经存在
    FileErr     = 104   # 上传文件出错
    ListNull    = 200   # 结果列表为空
    DBErr       = 300   # 数据库操作出现错误
    RegInfoErr  = 301   # 注册用户信息有错
    ReviseErr   = 302
    MsgFormErr  = 303
    UserIDErr   = 304   # UserID不在session里
    Error       = 400
    UnSupport   = 401
    Debug       = 500
    pass