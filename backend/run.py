# -*- coding=utf-8 -*-
from flask import Flask, g
# from controller import QiniuConfig, UserController, NoteController
from context import connect2db
from context.config import CurConfig
from context.Viewfunc import ViewFuncs


app = Flask(__name__)
app.config.from_object(CurConfig)  # 导入配置


# 注册视图函数
for (url, func) in ViewFuncs.items():
    app.add_url_rule(url, view_func=func, methods=['POST'])



# 关闭数据库连接
@app.teardown_appcontext
def closeDB(err):
    if hasattr(g, 'db'):
        g.db.close()


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
