# -*- coding=utf-8 -*-
from context.DBContext import DBContext


# 检查该用户名是否存在于系统中，返回是否
def check_account(account):
    sql_check_acct = "select uid from user where account=%s;"
    with DBContext() as context:
        context.exec(sql_check_acct, (account,))
        res = context.fetchone()
        return True if res else False
    pass


# 检查账户密码是否匹配，并获取用户id
def check_login(account, password):
    sql_login = "select uid,account,name from user where account=%s and password=%s;"
    with DBContext() as context:
        context.exec(sql_login, (account, password))
        res = context.fetchone()
        return res


# 新增一个用户
def add_user(account, password):
    sql_add_user = "insert into user(account, password, name) values (%s,%s,%s);"
    with DBContext() as db:
        res = db.exec(sql_add_user, (account, password, ''))
        return not db.is_error()


# 获取用户信息
def get_userinfo(uid):
    sql_get_userinfo = "select account, name from user where uid=%s;"
    with DBContext() as context:
        context.exec(sql_get_userinfo, (uid, ))
        res = context.get_cursor().fetchone()
        return res


# 修改用户名称
def set_username(id, name):
    sql_set_name = "update user set name=%s where uid=%s;"
    with DBContext() as context:
        context.exec(sql_set_name, (name, id))
        return not context.is_error()


# 修改用户密码
def set_password(id, password):
    sql_set_password = "update user set password=%s where uid=%s;"
    with DBContext() as context:
        context.exec(sql_set_password, (password, id))
        return not context.is_error()
