# -*- coding=utf-8 -*-
from flask import session
from model.Enum import Status
from model.Result import Result
from manager import UserManager
from controller.Adaptor import Controller, RequireAuth


admin_pwd = '123456'


# 登录接口
@Controller('account', 'password')
def login(account, password):
    res = UserManager.check_login(account, password)
    print(res)
    if res and 'uid' in res:
        session['userid'] = res['uid']
        session.permanent = True
        del res['uid']
        return Result(Status.OK, **res)
    else:
        return Result(Status.Error, msg='账号或密码错误')


# 注册接口
@Controller('admin', 'account', 'password')
def register(admin, account, password):
    # 对注册接口进行管理权限验证
    if admin != admin_pwd:
        return Result(Status.AuthErr, msg="权限错误")
    # 先判断account是否已经存在
    judge = UserManager.check_account(account)
    if judge:
        return Result(Status.AcctExist, msg="用户名已经存在")
    res = UserManager.add_user(account, password)
    if not res:
        return Result(Status.DBErr, msg="注册失败")
    return Result(Status.OK, msg="注册成功")


# 修改用户名称
@Controller('name')
@RequireAuth
def set_name(name):
    res = UserManager.set_username(session['userid'], name)
    return Result(Status.OK if res else Status.Error)


# 修改用户密码
@Controller('password')
@RequireAuth
def set_password(password):
    res = UserManager.set_password(session['userid'], password)
    return Result(Status.OK if res else Status.Error)


# 检查登录是否有效
@Controller()
@RequireAuth
def check():
    res = UserManager.get_userinfo(session['userid'])
    return res


# 登出
@Controller()
def logout():
    if 'userid' in session:
        del session['userid']
    return Result(Status.OK)
