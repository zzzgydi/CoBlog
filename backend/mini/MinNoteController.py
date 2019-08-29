# -*- coding=utf-8 -*-
from flask import session
from model.Enum import Status
from model.Result import Result
from mini import MinNoteManager as note
from controller.Adaptor import Controller


# state参数仅有的值
CONST_STATE = ('save', 'temp', 'del')


# 添加新的笔记
@Controller('label', 'title', 'content', 'state')
def add_note(label, title, content, state):
    if state not in CONST_STATE:
        return Result(Status.StatusErr, msg='参数state有误')
    res = note.add_note(label, title, content, state)
    if res:
        return Result(Status.OK)
    else:
        return Result(Status.Error)
    pass


# 修改笔记内容
@Controller('noteid', 'label', 'title', 'content', 'state')
def update_note(noteid, label, title, content, state):
    if state not in CONST_STATE:
        return Result(Status.StatusErr, msg='参数state有误')
    res = note.update_note(noteid, label, title, content, state)
    if res:
        return Result(Status.OK)
    else:
        return Result(Status.Error)
    pass


# 获取笔记内容
@Controller('noteid')
def view_note(noteid):
    res = note.get_note(noteid)
    if res and res['state'] not in CONST_STATE:
        return Result(Status.Error)
    if res:
        return Result(Status.OK, **res)
    return Result(Status.Error)


# 获取所有笔记的内容
@Controller('state')
def get_allnotes(state):
    if state not in CONST_STATE:
        return Result(Status.StatusErr, msg='参数state有误')
    res = note.get_allnotes(state)
    for r in res:
        r['content'] = r['content'][0:100]
    return Result(Status.OK, notes=res)


# 修改笔记状态
@Controller('noteid', 'state')
def revise_state(noteid, state):
    if state not in CONST_STATE:
        return Result(Status.StatusErr, msg='参数state有误')
    res = note.revise_state(noteid, state)
    if res:
        return Result(Status.OK)
    return Result(Status.Error)


# 新增标签
@Controller('value', 'color')
def add_label(value, color):
    res = note.add_label(value, color)
    if res:
        return Result(Status.OK)
    else:
        return Result(Status.Error)


# 获取所有标签
@Controller()
def get_labels():
    res = note.get_labels()
    return Result(Status.OK, labels=res)