# -*- coding=utf-8 -*-
'''
@Author: GyDi
@Date: 2018-12-01 21:11:30
@Description:  这里就放一些工具函数
'''

#将从数据中获得的数据, 从元组变成字典
def tuple2dict(keys, vals):
    res = dict()
    if len(keys) != len(vals):
        return None
    for key, val in zip(keys, vals):
        res[key] = val
    return res


def list2dict(keys, val_list):
    ress = []
    for val in val_list:
        tmp = tuple2dict(keys, val)
        if not tmp:
            raise Exception("GYDI ERROR")
        ress.append(tmp)
    return ress

