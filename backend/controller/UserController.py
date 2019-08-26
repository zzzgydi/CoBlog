# -*- coding=utf-8 -*-
from flask import session, request, jsonify
from model.Enum import Status
from model.Result import Result
from manager import UserManager
from controller.Adaptor import Controller
import json


# 登录接口
@Controller('account', 'password')
def login(account, password):
    res = UserManager.check_login(account, password)
    if res.status == Status.OK:
        session['id'] = res.getItem('id')
    return res


# 注册接口
@Controller('account', 'password')
def register(account, password):
    # 先判断account是否已经存在
    judge = UserManager.check_account(account)
    if judge:
        return Result(Status.AcctExist, msg="用户名已经存在")
    res = UserManager.add_user(account, password)
    if not res:
        return Result(Status.DBErr, msg="注册失败")
    return Result(Status.OK, msg="注册成功")
