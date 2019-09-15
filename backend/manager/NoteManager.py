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
        db.exec(sql_add_note,
                (noteid, userid, label, title, content, modified, state))
        return not db.is_error()


# 修改笔记内容
def update_note(userid, nid, label, title, content, state):
    sql_update = '''update note 
        set label=%s, title=%s, content=%s, modified=%s, state=%s
        where nid=%s and author=%s;'''
    modified = getTimeStamp()
    with DBContext() as context:
        res = context.exec(
            sql_update, (label, title, content, modified, state, nid, userid))
        if res == 1 and not context.is_error():
            return True
        return False


# 获取笔记内容 - 这里会获取作者的id，作者的名称
def get_note(nid):
    sql_get_note = '''select nid,author,label,title,content,modified,state,look,user.name,user.account,user.avatar
        from note join user on note.author=user.uid where nid=%s;'''
    with DBContext() as context:
        context.exec(sql_get_note, (nid, ))
        res = context.get_cursor().fetchone()
        return res


# 获取所有笔记的内容 列表 - 用于首页, 展示所有人的保存了的
def get_allnotes():
    sql_get_allnotes = '''
        select note.nid, label, title, modified, content, look, user.name
        from note inner join user
        on note.author=user.uid
        where state="save"
        order by look desc, modified desc;'''
    with DBContext() as context:
        context.exec(sql_get_allnotes)
        res = context.get_cursor().fetchall()
        return res


# 获取目录
def get_catalogue():
    sql_cata = '''select nid, label, title from note where state="save";'''
    with DBContext() as db:
        db.exec(sql_cata)
        res = db.fetchall()
        return res


# 获取用户的所有笔记 列表 - 可分状态
def get_usernotes(userid, state):
    sql_get_usernotes = '''
        select nid, label, title, modified, content, look from note
        where author=%s and state=%s
        order by modified desc;'''
    with DBContext() as context:
        context.exec(sql_get_usernotes, (userid, state))
        res = context.get_cursor().fetchall()
        return res
    pass


# 获取我的笔记包括save和私人
def get_usernotes_mine(userid):
    sql_get_mine = '''
        select nid, label, title, modified, content, state, look from note
        where author=%s and (state="self" or state="save")
        order by modified desc;'''
    with DBContext() as context:
        context.exec(sql_get_mine, (userid, ))
        res = context.get_cursor().fetchall()
        return res
    pass


# 根据账户名获取用户公开的笔记
def get_page_notes(user):
    sql_get_author = "select uid from user where account=%s;"
    sql_page_notes = '''
        select nid, label, title, modified, content, state, look from note
        where author=%s and state="save" order by look desc;'''
    with DBContext() as db:
        db.exec(sql_get_author, (user, ))
        author = db.fetchone()
        if not author: return None
        db.exec(sql_page_notes, (author['uid'], ))
        notes = db.fetchall()
        for note in notes:
            note['content'] = note['content'][0:180] 
        return notes


# 观看一次笔记
def look_note(noteid):
    sql_look = "update note set look=look+1 where nid=%s;"
    with DBContext() as db:
        db.exec(sql_look, (noteid, ))
        return not db.is_error()


# 修改笔记状态
def revise_state(userid, nid, state):
    sql_revise_state = '''
        update note set state=%s
        where nid=%s and author=%s;'''
    with DBContext() as context:
        res = context.exec(sql_revise_state, (state, nid, userid))
        return not context.is_error()


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
    sql_get_lid = "select l_id from label where user=%s and value=%s;"
    with DBContext() as context:
        res = context.exec(sql_add_label, (userid, value, color))
        if res == 1:
            context.exec(sql_get_lid, (userid, value))
            res = context.fetchone()
            return res
        else:
            return False


# 获取所有的标签
def get_labels(userid):
    sql_get_labels = "select l_id, value from label where user=%s;"
    with DBContext() as context:
        context.exec(sql_get_labels, (userid, ))
        res = context.get_cursor().fetchall()
        return res


# 删除标签
def del_label(userid, lid):
    sql_del_label = "delete from label where l_id=%s and user=%s;"
    with DBContext() as db:
        db.exec(sql_del_label, (lid, userid))
        return not db.is_error()


# 添加收藏链接
def add_url(user, title, url, desc):
    sql_add_url = 'insert into favurl(user, title, url, remark, modified) values(%s,%s,%s,%s,%s);'
    modified = getTimeStamp()
    with DBContext() as db:
        db.exec(sql_add_url, (user, title, url, desc, modified))
        return not db.is_error()


# 删除收藏链接
def del_url(fid, user):
    sql_del_url = "delete from favurl where fid=%s and user=%s;"
    with DBContext() as db:
        db.exec(sql_del_url, (fid, user))
        return not db.is_error()
    pass


# 获取所有链接
def all_url(user):
    sql_all_url = "select fid,title,url,remark,modified from favurl where user=%s order by modified desc;"
    with DBContext() as db:
        db.exec(sql_all_url, (user, ))
        res = db.fetchall()
        return res
    pass


# 查看链接
def get_url(fid, user):
    sql_get = "select fid,title,url,remark,modified from favurl where fid=%s and user=%s;"
    with DBContext() as db:
        db.exec(sql_get, (fid, user))
        res = db.fetchone()
        return res
    pass
