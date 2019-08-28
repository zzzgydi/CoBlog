# -*- coding=utf-8 -*-
from context.DBContext import DBContext
from model.Enum import Status
from model.Result import Result
from model.Tool import *
import hashlib
import time

'''
最小版
'''


sql_add_note = '''
    insert into note(label, title, content, modified, state) 
    values(?,?,?,?,?);
    '''
sql_update_note = '''
    update note set label=?, title=?, content=?, modified=?, state=?
    where id=?;
    '''
sql_get_note = '''
    select * from note
    where id=?;
    '''
sql_get_allnotes = '''
    select * from note
    where state=?
    order by label, modified desc;
    '''
key_note = ('id', 'label', 'title', 'content', 'modified', 'state')


# 添加新的笔记
def add_note(label, title, content, state):
    modified = str(time.time())
    with DBContext() as context:
        context.exec(sql_add_note, (label, title, content, modified, state))
        return not context.is_error()


# 修改笔记内容
def update_note(nid, label, title, content, state):
    modified = str(time.time())
    with DBContext() as context:
        context.exec(sql_update_note, (label, title, content, modified, state, nid))
        return not context.is_error()


# 获取笔记内容
def get_note(nid):
    with DBContext() as context:
        context.exec(sql_get_note, (nid, ))
        res = context.get_cursor().fetchone()
        if not res:
            return None
        res = tuple2dict(key_note, res)
        return res


# 获取所有笔记的内容
def get_allnotes(state):
    with DBContext() as context:
        context.exec(sql_get_allnotes, (state, ))
        res = context.get_cursor().fetchall()
        return list2dict(key_note, res)