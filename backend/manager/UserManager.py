# -*- coding=utf-8 -*-
from context.DBContext import DBContext
from model.Enum import Status
from model.Result import Result
from model.Tool import tuple2dict, list2dict, getTimeStamp
import manager.SQL as sql
import hashlib
# import time

sql_check_acct = '''
    select * from user
    where account=?;'''
sql_check_login = '''
    select id from user
    where account=? and password=?;'''
sql_add_user = '''
    insert into user(id, account, password, name)
    values (?,?,?,?);'''
sql_get_userinfo = '''
    select account, name from user
    where id=?;'''
sql_set_name = '''
    update user set name=?
    where id=?;'''
sql_set_password = '''
    update user set password=?
    where id=?;'''


key_user = ('id', 'account', 'password', 'name')


# 检查该用户名是否存在于系统中，返回是否
def check_account(account):
    with DBContext() as context:
        context.exec(sql_check_acct, (account,))
        res = context.get_cursor().fetchone()
        return True if res else False
    pass


# 检查账户密码是否匹配，并获取用户id
def check_login(account, password):
    with DBContext() as context:
        context.exec(sql_check_login, (account,password))
        res = context.get_cursor().fetchone()
        if not res:
            return Result(Status.Error)  # 返回登录错误
        userid = res[0]
        context.exec(sql_get_userinfo, (userid, ))
        res = context.get_cursor().fetchone()
        return Result(Status.OK, id=userid, account=res[0], name=res[1])


# 新增一个用户
def add_user(account, password):
    md5 = hashlib.md5(str(getTimeStamp()).encode('utf-8'))
    randid = md5.hexdigest()
    with DBContext() as context:
        context.exec(sql_add_user, (randid, account, password, ''))
        return not context.is_error()


# 获取用户信息
def get_userinfo(uid):
    with DBContext() as context:
        context.exec(sql_get_userinfo, (uid, ))
        res = context.get_cursor().fetchone()
        if not res:
            return Result(Status.IdErr)  # 返回登录错误
        res = tuple2dict(('account', 'name'), res)
        return Result(Status.OK, **res)


# 修改用户名称
def set_username(id, name):
    with DBContext() as context:
        context.exec(sql_set_name, (name, id))
        return not context.is_error()


# 修改用户密码
def set_password(id, password):
    with DBContext() as context:
        context.exec(sql_set_password, (password, id))
        return not context.is_error()
