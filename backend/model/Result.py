# -*- coding=utf-8 -*-


# 用于构造响应体数据对象
class Result():
    def __init__(self, status, **kwargs):
        self.status = status
        self.msg = ''
        self.data = {}
        if kwargs and 'msg' in kwargs:
            self.msg = kwargs['msg']
            del kwargs['msg']
        for key in kwargs:
            self.data[key] = kwargs[key]

    def setItem(self, key, value):
        self.data[key] = value

    def setMore(self, **kwargs):
        for key in kwargs:
            self.data[key] = kwargs[key]

    def getItem(self, key):
        return self.data.get(key)

    def toDict(self):
        return {
            'status': self.status,
            'msg': self.msg,
            'data': self.data
        }
    