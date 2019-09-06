# -*- coding=utf-8 -*-
from context.DBContext import DBContext
from model.Tool import getTimeStamp, randStr
import hashlib


# 添加新的笔记
def add_note(userid, label, title, content, state):
    sql_add_note = '''
        insert into note(nid, author, label, title, content, modified, state)
        values(%s,%s,%s,%s,%s,%s,%s);'''
    modified = getTimeStamp()
    noteid = 'n' + randStr(8)  # 产生笔记的id
    with DBContext() as db:
        db.exec(sql_add_note, (noteid, userid, label, title, content, modified, state))
        return not db.is_error()


# 修改笔记内容
def update_note(userid, nid, label, title, content, state):
    sql_update = '''update note 
        set label=%s, title=%s, content=%s, modified=%s, state=%s
        where nid=%s and author=%s;'''
    modified = getTimeStamp()
    with DBContext() as context:
        res = context.exec(sql_update, (label, title,
                                        content, modified, state, nid, userid))
        if res == 1 and not context.is_error():
            return True
        return False


# 获取笔记内容 - 这里会获取作者的id，作者的名称
def get_note(nid):
    sql_get_note = '''select nid,author,label,title,content,modified,state,user.name 
        from note join user on note.author=user.uid where nid=%s;'''
    with DBContext() as context:
        context.exec(sql_get_note, (nid, ))
        res = context.get_cursor().fetchone()
        return res


# 获取所有笔记的内容 列表 - 用于首页, 展示所有人的保存了的
def get_allnotes():
    sql_get_allnotes = '''
        select note.nid, label, title, modified, content, user.name
        from note inner join user
        on note.author=user.uid
        where state="save"
        order by modified desc;'''
    with DBContext() as context:
        context.exec(sql_get_allnotes)
        res = context.get_cursor().fetchall()
        return res


# 获取用户的所有笔记 列表 - 可分状态
def get_usernotes(userid, state):
    sql_get_usernotes = '''
        select nid, label, title, modified, content from note
        where author=%s and state=%s
        order by modified desc;'''
    with DBContext() as context:
        context.exec(sql_get_usernotes, (userid, state))
        res = context.get_cursor().fetchall()
        return res
    pass


# 修改笔记状态
def revise_state(userid, nid, state):
    sql_revise_state = '''
        update note set state=%s
        where nid=%s and author=%s;'''
    with DBContext() as context:
        res = context.exec(sql_revise_state, (state, nid, userid))
        if res == 1 and not context.is_error():
            return True
        return False


# 永久删除笔记
def delete_note(userid, noteid):
    sql_delete_note = '''
        delete from note
        where author=%s and nid=%s and state='del';
        '''
    with DBContext() as context:
        context.exec(sql_delete_note, (userid, noteid))
        return not context.is_error()


# 新增标签
def add_label(userid, value, color):
    sql_add_label = "insert into label(user, value, color) values(%s,%s,%s);"
    with DBContext() as context:
        context.exec(sql_add_label, (userid, value, color))
        return not context.is_error()


# 获取所有的标签
def get_labels(userid):
    sql_get_labels = "select value from label where user=%s;"
    with DBContext() as context:
        context.exec(sql_get_labels, (userid, ))
        res = context.get_cursor().fetchall()
        rlist = []
        for t in res:
            rlist.append(t['value'])
        return rlist
