# -*- coding=utf-8 -*-
from context.DBContext import DBContext
from context import get_db
from model.Enum import Status
from model.Result import Result
from model.Tool import tuple2dict, list2dict, getTimeStamp
import manager.SQL as sql
import hashlib
# import time

sql_check_acct = '''
    select * from user
    where account=%s;'''
sql_login = '''
    select uid, account, name from user
    where account=%s and password=%s;'''
sql_check_login = '''
    select uid from user
    where account=%s and password=%s;'''
sql_add_user = '''
    insert into user(uid, account, password, name)
    values (%s,%s,%s,%s);'''
sql_get_userinfo = '''
    select account, name from user
    where uid=%s;'''
sql_set_name = '''
    update user set name=%s
    where uid=%s;'''
sql_set_password = '''
    update user set password=%s
    where uid=%s;'''


key_user = ('uid', 'account', 'password', 'name')


# 检查该用户名是否存在于系统中，返回是否
def check_account(account):
    with DBContext() as context:
        context.exec(sql_check_acct, (account,))
        res = context.get_cursor().fetchone()
        return True if res else False
    pass


# # 检查账户密码是否匹配，并获取用户id
# def check_login(account, password):
#     with DBContext() as context:
#         context.exec(sql_check_login, (account,password))
#         res = context.get_cursor().fetchone()
#         print(res)
#         if not res:
#             return Result(Status.Error)  # 返回登录错误
#         userid = res['uid']
#         context.exec(sql_get_userinfo, (userid, ))
#         res = context.get_cursor().fetchone()
#         print(res)
#         return Result(Status.OK, id=userid, account=res['account'], name=res['name'])


# 检查账户密码是否匹配，并获取用户id
def check_login(account, password):
    with DBContext() as context:
        # context.exec(sql_login, (account,password))
        context.exec('select * from user;')
        res = context.get_cursor().fetchall()
        return res
        

# # 新增一个用户
# def add_user(account, password):
#     md5 = hashlib.md5(str(getTimeStamp()).encode('utf-8'))
#     randid = md5.hexdigest()
#     with DBContext() as context:
#         context.exec(sql_add_user, (randid, account, password, ''))
#         return not context.is_error()


# 新增一个用户
def add_user(account, password):
    with DBContext() as db:
        res = db.exec("insert into user(account, password, name) values (%s,%s,%s);", (account, password, ''))
        return not db.is_error()


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
