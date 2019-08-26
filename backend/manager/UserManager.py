# -*- coding=utf-8 -*-
from context.DBContext import DBContext
from model.Enum import Status
from model.Result import Result
from model.Tool import *
import manager.SQL as sql
import hashlib
import time


# 检查该用户名是否存在于系统中，返回是否
# 检查账户密码是否匹配，并获取用户id
# 新增一个用户
# 获取用户信息
# 修改用户名称


# 检查该用户名是否存在于系统中，返回是否
def check_account(account):
    with DBContext() as context:
        context.exec(sql.sql_check_acct, (account,))
        res = context.get_cursor().fetchone()
        return True if res else False
    pass


# 检查账户密码是否匹配，并获取用户id
def check_login(account, password):
    with DBContext() as context:
        context.exec(sql.sql_check_login, (account,password))
        res = context.get_cursor().fetchone()
        if not res:
            return Result(Status.LoginErr)  # 返回登录错误
        res = tuple2dict(sql.key_user, res)
        return Result(Status.OK, id=res['id'], account=res['account'], name=res['name'])


# 新增一个用户
def add_user(account, password):
    md5 = hashlib.md5(str(time.time()).encode('utf-8'))
    randid = md5.hexdigest()
    with DBContext() as context:
        context.exec(sql.sql_add_user, (randid, account, password, ''))
        return not context.is_error()


# 获取用户信息
def get_userinfo(id):
    with DBContext() as context:
        context.exec(sql.sql_get_userinfo, (id, ))
        res = context.get_cursor().fetchone()
        if not res:
            return Result(Status.IdErr)  # 返回登录错误
        res = tuple2dict(sql.key_user, res)
        return Result(Status.OK, id=res['id'], account=res['account'], name=res['name'])


# 修改用户名称
def set_username(id, name):
    with DBContext() as context:
        context.exec(sql.sql_set_name, (name, id))
        return not context.is_error()
