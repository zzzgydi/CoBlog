# -*- coding=utf-8 -*-
from context.DBContext import DBContext
from model.Enum import Status
from model.Result import Result
from model.Tool import *
import manager.SQL as sql
import hashlib
import time


# 创建新的笔记本
# 添加合作者
# 删除合作者
# 获取某笔记本的信息
# 获取某人所有笔记本
# 获取某笔记本所有笔记
# 获取某笔记本某类型所有笔记


# 创建新的笔记本
def add_book(creator, visible, desc):
    md5 = hashlib.md5(str(time.time()).encode('utf-8'))
    bookid = 'b' + md5.hexdigest()
    with DBContext() as context:
        context.exec(sql.sql_add_book, (bookid, visible, creator, str(time.time()), desc))
        if context.is_error(): return None
        context.exec(sql.sql_add_bookuser, (creator, bookid))
        return bookid if not context.is_error() else None


# 添加合作者
def add_cooperator(user, bookid) -> bool:
    with DBContext() as context:
        context.exec(sql.sql_add_bookuser, (user, bookid))
        return not context.is_error()


# 删除合作者
def remove_cooperator(user, bookid):
    with DBContext() as context:
        context.exec(sql.sql_find_creator, (bookid,))
        res = context.get_cursor().fetchone()
        if not res:     # 找不到该书
            return False
        if res[0] == user:  # 创建者不可以被删除
            return False
        context.exec(sql.sql_del_bookuser, (user, bookid))
        return not context.is_error()