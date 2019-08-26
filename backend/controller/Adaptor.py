# -*- coding=utf-8 -*-

from model.Result import Result
from model.Enum import Status
from flask import jsonify, request
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
            data = json.loads(request.data)
            for key in args:
                if key not in data:
                    return jsonifyResult(Result(Status.FormErr, msg='Missing Parameters ' + key))
            return jsonifyResult(func(**data))
        return wrapper
    return outter