# -*- coding=utf-8 -*-
from context.DBContext import DBContext
from model.Enum import Status
from model.Result import Result
from model.Tool import list2dict, tuple2dict, getTimeStamp
import hashlib
# import time


sql_add_note = '''
    insert into note(author, label, title, content, modified, state) 
    values(?,?,?,?,?,?);'''
sql_get_author = '''
    select author from note
    where id=?;'''
sql_update_note = '''
    update note set label=?, title=?, content=?, modified=?, state=?
    where id=?;'''
sql_get_note = '''
    select * from note
    where id=?;'''
sql_get_allnotes = '''
    select note.id, label, title, modified, content, user.name
    from note inner join user
    on note.author=user.id
    where state="save"
    order by modified desc;'''
sql_get_usernotes = '''
    select id, label, title, modified, content from note
    where author=? and state=?
    order by modified desc;'''
sql_revise_state = '''
    update note set state=?
    where id=?;'''
sql_delete_note = '''
    delete from note
    where author=? and id=? and state='del';
    '''
sql_get_labels = '''
    select value from label
    where user=?;'''
sql_add_label = '''
    insert into label(user, value, color)
    values(?,?,?);'''
sql_user_name = '''
    select name from user
    where id=?;'''

key_note = ('id', 'authorid', 'label', 'title', 'content', 'modified', 'state')
key_note_min = ('id', 'label', 'title', 'modified', 'content')
key_note_list = ('id', 'label', 'title', 'modified', 'content', 'author')


# 添加新的笔记
def add_note(userid, label, title, content, state):
    # modified = str(time.time())
    modified = getTimeStamp()
    with DBContext() as context:
        context.exec(sql_add_note, (userid, label, title, content, modified, state))
        return not context.is_error()


# 修改笔记内容
def update_note(userid, nid, label, title, content, state):
    # modified = str(time.time())
    modified = getTimeStamp()
    with DBContext() as context:
        context.exec(sql_get_author, (nid, ))
        res = context.get_cursor().fetchone()
        if not res:    # 说明该id不在数据库中
            return Status.Error
        if res[0] != userid:    # 说明修改人和作者不是同一个
            return Status.AuthErr
        context.exec(sql_update_note, (label, title, content, modified, state, nid))
        return Status.OK if not context.is_error() else Status.DBErr


# 获取笔记内容 - 这里会获取作者的id，作者的名称
def get_note(nid):
    with DBContext() as context:
        context.exec(sql_get_note, (nid, ))
        res = context.get_cursor().fetchone()
        if not res: return None
        res = tuple2dict(key_note, res)
        context.exec(sql_user_name, (res['authorid'], ))
        name = context.get_cursor().fetchone()
        if not name: 
            name = ''
        res['author'] = name[0]
        return res


# 获取所有笔记的内容 列表 - 用于首页, 展示所有人的保存了的
def get_allnotes():
    with DBContext() as context:
        context.exec(sql_get_allnotes)
        res = context.get_cursor().fetchall()
        return list2dict(key_note_list, res)


# 获取用户的所有笔记 列表 - 可分状态
def get_usernotes(userid, state):
    with DBContext() as context:
        context.exec(sql_get_usernotes, (userid, state))
        res = context.get_cursor().fetchall()
        return list2dict(key_note_min, res)
    pass


# 修改笔记状态
def revise_state(userid, nid, state):
    with DBContext() as context:
        context.exec(sql_get_author, (nid, ))
        res = context.get_cursor().fetchone()
        if not res:    # 说明该id不在数据库中
            return Status.Error
        if res[0] != userid:    # 说明修改人和作者不是同一个
            return Status.AuthErr
        context.exec(sql_revise_state, (state, nid))
        return Status.OK if not context.is_error() else Status.DBErr


# 永久删除笔记
def delete_note(userid, noteid):
    with DBContext() as context:
        context.exec(sql_delete_note, (userid, noteid))
        return Status.OK if not context.is_error() else Status.DBErr


# 新增标签
def add_label(userid, value, color):
    with DBContext() as context:
        context.exec(sql_add_label, (userid, value, color))
        return not context.is_error()


# 获取所有的标签
def get_labels(userid):
    with DBContext() as context:
        context.exec(sql_get_labels, (userid, ))
        res = context.get_cursor().fetchall()
        rlist = []
        for t in res:
            rlist.append(t[0])
        return rlist
