# -*- coding=utf-8 -*-
'''
@Author: GyDi
@Description: 声明包
'''

import pymysql
from flask import g
from context.config import CurConfig

# 获得数据库的连接
def connect2db(host, port, user, pwd, db):
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=pwd,
        database=db,
        charset="utf8"
    )
    return conn


# 获得db对象
def get_db():
    db = getattr(g, 'db', None)
    if not db:
        g.db = connect2db(host=CurConfig.DB_HOST, port=CurConfig.DB_PORT,
                        user=CurConfig.DB_USER, pwd=CurConfig.DB_PWD, db=CurConfig.DB_NAME)
    return g.db
