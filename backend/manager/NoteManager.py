# -*- coding=utf-8 -*-
from context.DBContext import DBContext
from model.Enum import Status
from model.Result import Result
from model.Tool import *
import manager.SQL as sql
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
    select id, label, title, modified, content from note
    where state=?
    order by modified desc;
    '''
sql_revise_state = '''
    update note set state=?
    where id=?;
    '''
sql_get_labels = '''
    select value from label;
    '''
sql_add_label = '''
    insert into label(value, color)
    values(?, ?);
    '''

key_note = ('id', 'label', 'title', 'content', 'modified', 'state')
key_note_min = ('id', 'label', 'title', 'modified', 'content')

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


# 获取所有笔记的内容列表
def get_allnotes(state):
    with DBContext() as context:
        context.exec(sql_get_allnotes, (state, ))
        res = context.get_cursor().fetchall()
        return list2dict(key_note_min, res)


# 修改笔记状态
def revise_state(nid, state):
    with DBContext() as context:
        context.exec(sql_revise_state, (state, nid))
        return not context.is_error()


# 新增标签
def add_label(value, color):
    with DBContext() as context:
        context.exec(sql_add_label, (value, color))
        return not context.is_error()


# 获取所有的标签
def get_labels():
    with DBContext() as context:
        context.exec(sql_get_labels)
        res = context.get_cursor().fetchall()
        rlist = []
        for t in res:
            rlist.append(t[0])
        return rlist
