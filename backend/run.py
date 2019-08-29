# -*- coding=utf-8 -*-
from datetime import timedelta
from flask import Flask, request, render_template, jsonify
from model.Result import Result
# from controller import UserController
from mini import MinNoteController, QiniuConfig

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")


app.config['SECRET_KEY'] = "MIN1234567890"
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=3)

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
# 	return render_template("index.html")

# app.add_url_rule('/api/login', view_func=UserController.login, methods=['POST'])
# app.add_url_rule('/api/register', view_func=UserController.register, methods=['POST'])

app.add_url_rule('/api/addnote', view_func=MinNoteController.add_note, methods=['POST'])
app.add_url_rule('/api/getnotes', view_func=MinNoteController.get_allnotes, methods=['POST'])
app.add_url_rule('/api/viewnote', view_func=MinNoteController.view_note, methods=['POST'])
app.add_url_rule('/api/updatenote', view_func=MinNoteController.update_note, methods=['POST'])
app.add_url_rule('/api/notestate', view_func=MinNoteController.revise_state, methods=['POST'])
app.add_url_rule('/api/addlabel', view_func=MinNoteController.add_label, methods=['POST'])
app.add_url_rule('/api/getlabels', view_func=MinNoteController.get_labels, methods=['POST'])

app.add_url_rule('/api/gettoken', view_func=QiniuConfig.get_token, methods=['POST'])


if __name__ =="__main__":
	app.run(debug=False, host='0.0.0.0')
