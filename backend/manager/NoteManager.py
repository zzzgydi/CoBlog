# -*- coding=utf-8 -*-
from context.DBContext import DBContext
from model.Enum import Status
from model.Result import Result
from model.Tool import *
import manager.SQL as sql
import hashlib
import time


# 添加新的笔记
# 修改笔记内容
# 获取笔记内容


# 添加新的笔记
def add_note(bookid, label, title, content, user, state):
    modified = str(time.time())
    with DBContext() as context:
        context.exec(sql.sql_add_note, (bookid,label,title,content, modified,user, state))
        return not context.is_error()


# 修改笔记内容
def update_note(nid, bookid, label, title, content, user, state):
    modified = str(time.time())
    with DBContext() as context:
        context.exec(sql.sql_update_note, (label, title, content, modified, user, state, nid, bookid))
        return not context.is_error()


# 获取笔记内容
def get_note(nid, bookid):
    with DBContext() as context:
        context.exec(sql.sql_get_note, (nid, bookid))
        res = context.get_cursor().fetchone()
        if not res:
            return None
        res = tuple2dict(sql.key_note, res)
        return res