# -*- coding=utf-8 -*-
'''
@Author: GyDi
@Date: 2018-12-01 21:11:30
@Description:  这里就放一些工具函数
'''
import random
import os
import datetime
import time


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


# 获取时间戳 - 返回整数
def getTimeStamp():
    return int(time.time() * 1000)


# 生成随机字符串，验证过8位的抗碰撞很可以
def randStr(n):
    return (''.join(map(lambda xx: (hex(xx)[2:]), os.urandom(n))))[0:16]


if __name__ == '__main__':
    # print(hex(int(tid_maker())))
    se = set()
    for i in range(50):
        # se.add(randStr(8))
        print(randStr(8))
    print(len(se))
    pass
