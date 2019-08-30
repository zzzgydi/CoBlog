# -*- coding=utf-8 -*-
from datetime import timedelta
from flask import Flask, request, render_template, jsonify
from model.Result import Result
from controller import QiniuConfig, UserController, NoteController
# from mini import MinNoteController

app = Flask(__name__, static_folder = "./dist/static", template_folder = "./dist")


app.config['SECRET_KEY'] = "CONOTE1234567890B"
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=3)


# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
# 	return render_template("index.html")

app.add_url_rule('/api/login', view_func=UserController.login, methods=['POST'])
app.add_url_rule('/api/register', view_func=UserController.register, methods=['POST'])
app.add_url_rule('/api/check', view_func=UserController.check, methods=['POST'])    # 检查登录是否有效
app.add_url_rule('/api/logout', view_func=UserController.logout, methods=['POST'])


app.add_url_rule('/api/addnote', view_func=NoteController.add_note, methods=['POST'])
app.add_url_rule('/api/getnotes', view_func=NoteController.get_allnotes, methods=['POST'])  # 首页获取
app.add_url_rule('/api/usernotes', view_func=NoteController.get_usernotes, methods=['POST']) # 用户页获取
app.add_url_rule('/api/viewnote', view_func=NoteController.view_note, methods=['POST'])
app.add_url_rule('/api/updatenote', view_func=NoteController.update_note, methods=['POST'])
app.add_url_rule('/api/notestate', view_func=NoteController.revise_state, methods=['POST'])
app.add_url_rule('/api/addlabel', view_func=NoteController.add_label, methods=['POST'])
app.add_url_rule('/api/getlabels', view_func=NoteController.get_labels, methods=['POST'])

app.add_url_rule('/api/gettoken', view_func=QiniuConfig.get_token, methods=['POST'])


if __name__ =="__main__":
	app.run(debug=False, host='0.0.0.0')
