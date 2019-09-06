# -*- coding=utf-8 -*-
from flask import session
from model.Enum import Status
from model.Result import Result
from manager import NoteManager as note
from controller.Adaptor import Controller, RequireAuth


# state参数仅有的值
CONST_STATE = ('save', 'self', 'temp', 'del')


# 添加新的笔记
@Controller('label', 'title', 'content', 'state')
@RequireAuth
def add_note(label, title, content, state):
    if state not in CONST_STATE:
        return Result(Status.StatusErr, msg='参数state有误')
    userid = session['userid']
    res = note.add_note(userid, label, title, content, state)
    return Result(Status.OK if res else Status.Error)
    pass


# 修改笔记内容
@Controller('noteid', 'label', 'title', 'content', 'state')
@RequireAuth
def update_note(noteid, label, title, content, state):
    if state not in CONST_STATE:
        return Result(Status.StatusErr, msg='参数state有误')
    userid = session['userid']
    res = note.update_note(userid, noteid, label, title, content, state)
    return Result(Status.OK if res else Status.Error)


# 获取笔记内容 - 对于不是自己的文章且状态不为save的，不通过
@Controller('noteid')
def view_note(noteid):
    res = note.get_note(noteid)
    if not res or res['state'] not in CONST_STATE:
        return Result(Status.Error)
    author = res['author']
    del res['author']
    if res['state'] == 'save' or session.get('userid', None) == author:
        return Result(Status.OK, **res)
    return Result(Status.AuthErr)   # 这里返回权限问题


# 获取所有笔记的列表
@Controller()
def get_allnotes():
    res = note.get_allnotes()
    for r in res:
        r['content'] = r['content'][0:200]  # 这里可以做内容缓存
    return Result(Status.OK, notes=res)


# 获取用户的笔记列表
@Controller('state')
@RequireAuth
def get_usernotes(state):
    if state not in CONST_STATE:
        return Result(Status.StatusErr, msg='参数state有误')
    res = note.get_usernotes(session['userid'], state)
    for r in res:
        r['content'] = r['content'][0:200]
    return Result(Status.OK, notes=res)


# 修改笔记状态
@Controller('noteid', 'state')
@RequireAuth
def revise_state(noteid, state):
    if state not in CONST_STATE:
        return Result(Status.StatusErr, msg='参数state有误')
    res = note.revise_state(session['userid'], noteid, state)
    return Result(Status.OK if res else Status.Error)


# 永久删除笔记
@Controller('noteid')
@RequireAuth
def delete_note(noteid):
    res = note.delete_note(session['userid'], noteid)
    return Result(Status.OK if res else Status.Error)


# 新增标签
@Controller('value', 'color')
@RequireAuth
def add_label(value, color):
    res = note.add_label(session['userid'], value, color)
    return Result(Status.OK if res else Status.Error)


# 获取所有标签
@Controller()
@RequireAuth
def get_labels():
    res = note.get_labels(session['userid'])
    return Result(Status.OK, labels=res)
