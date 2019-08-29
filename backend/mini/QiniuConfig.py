# -*- coding=utf-8 -*-
import os
import time
import hashlib
from qiniu import Auth
from controller.Adaptor import Controller
from model.Enum import Status
from model.Result import Result



access_key = 'nOXQexJojurXJVKHVc1Uxk4niiamm35vx-LGereZ'
secret_key = 'JCBWE4MsAGXFCzT0NOY_3obgR0aw-A5p4zj9B4SW'

q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = 'sehub'


# 获取上传的token
@Controller('filename')
def get_token(filename):
    key = str(time.time()) + filename   # 加盐
    _, ftype = os.path.splitext(filename)
    if len(ftype) == 0:
        return Result(Status.Error, msg="文件名格式有误")
    md5 = hashlib.md5(str(time.time()).encode('utf-8'))
    key = md5.hexdigest() + ftype   # 上传后保存的文件名

    #3600为token过期时间，秒为单位。3600等于一小时
    token = q.upload_token(bucket_name, key, 3600)
    return Result(Status.OK, token=token, key=key)

