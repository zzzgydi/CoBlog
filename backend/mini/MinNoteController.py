# -*- coding=utf-8 -*-
from flask import session, request, jsonify
from model.Enum import Status
from model.Result import Result
from mini import MinNoteManager as note
from controller.Adaptor import Controller
import json

# state参数仅有的值
CONST_STATE = ('save', 'temp', 'del', 'err')


# 添加新的笔记
@Controller('label', 'title', 'content', 'state')
def add_note(label, title, content, state):
    if state not in CONST_STATE:
        state = 'err'
    res = note.add_note(label, title, content, state)
    if res:
        return Result(Status.OK)
    else:
        return Result(Status.Error)
    pass


# 修改笔记内容
# 获取笔记内容


# 获取所有笔记的内容
@Controller('state')
def get_allnotes(state):
    if state not in CONST_STATE:
        return Result(Status.StatusErr, msg='参数state有误')
    res = note.get_allnotes(state)
    return Result(Status.OK, notes=res)