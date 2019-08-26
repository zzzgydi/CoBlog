# -*- coding=utf-8 -*-


# 用于构造响应体数据对象
class Result():
    def __init__(self, status, **kwargs):
        self.status = status
        self.data = {}
        for key in kwargs:
            self.data[key] = kwargs[key]

    def setItem(self, key, value):
        self.data[key] = value

    def setMore(self, **kwargs):
        for key in kwargs:
            self.data[key] = kwargs[key]

    def getItem(self, key):
        self.data.get(key)

    def toDict(self):
        return {
            'status': self.status,
            'data': self.data
        }
    