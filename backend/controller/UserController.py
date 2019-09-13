# -*- coding=utf-8 -*-
from flask import session
from model.Enum import Status
from model.Result import Result
from manager import UserManager
from context.config import CurConfig
from controller.Adaptor import Controller, RequireAuth
from model.RandImg import create_validate_code
import re


# 登录接口
@Controller('account', 'password')
def login(account, password):
    res = UserManager.check_login(account, password)
    if res and 'uid' in res:
        session['userid'] = res['uid']
        session.permanent = True
        del res['uid']
        return Result(Status.OK, **res)
    else:
        return Result(Status.Error, msg='账号或密码错误')


# 注册接口
@Controller('admin', 'account', 'password')
def admin_register(admin, account, password):
    # 对注册接口进行管理权限验证
    if admin != CurConfig.ADMIN_PWD:
        return Result(Status.AuthErr, msg="权限错误")
    # 先判断account是否已经存在
    judge = UserManager.check_account(account)
    if judge:
        return Result(Status.AcctExist, msg="用户名已经存在")
    res = UserManager.add_user(account, password)
    if not res:
        return Result(Status.DBErr, msg="注册失败")
    return Result(Status.OK, msg="注册成功")


# 注册接口
@Controller('account', 'password', 'code')
def register(account, password, code):
    if not ('randimg' in session
            and session['randimg'].upper() == code.upper()):
        return Result(Status.RegImgErr, msg="验证码有误")
    # 检查参数
    if len(account) < 4 or re.match("[^a-zA-Z0-9]", account):
        return Result(Status.RegAccErr, msg="账号格式有误")
    if len(password) < 6 or re.match("[^a-zA-Z0-9-*/+.~!@#$%^&*()_]",
                                     password):
        return Result(Status.RegPwdErr, msg="密码格式有误")
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
    if res:
        return Result(Status.OK, **res)
    else:
        return Result(Status.LoginReq)


# 登出
@Controller()
def logout():
    if 'userid' in session:
        del session['userid']
    return Result(Status.OK)


# 获得验证码
@Controller()
def get_randimg():
    img_str, code = create_validate_code()
    session['randimg'] = code
    return Result(Status.OK, img=img_str)
