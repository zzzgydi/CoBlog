# -*- coding=utf-8 -*-

from model.Result import Result
from model.Enum import Status
from flask import jsonify, request, session
from functools import wraps
import json


def jsonifyResult(obj):
    if isinstance(obj, Result):
        return jsonify(obj.toDict())
    else:
        return jsonify(obj)

# 控制器的装饰器
def Controller(*args):
    def outter(func):
        @wraps(func)
        def wrapper():
            if not (args and request.data):
                return jsonifyResult(func())
            data = json.loads(request.data)
            res = {}
            for key in args:
                if key not in data:
                    return jsonifyResult(Result(Status.FormErr, msg='Missing Parameters ' + key))
                res[key] = data[key]
            return jsonifyResult(func(**res))
        return wrapper
    return outter


# 登录权限约束 - 这里不是一个控制器，所以不返回jsonify
def RequireAuth(func):
    @wraps(func)
    def wrapper(**args):
        if 'userid' not in session:
            return Result(Status.LoginReq, msg='Require Login')
        return func(**args)
    return wrapper