# -*- coding=utf-8 -*-
from datetime import timedelta
from flask import Flask, request, render_template, jsonify
from model.Result import Result
# from controller import UserController
from mini import MinNoteController

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


if __name__ =="__main__":
	app.run(debug=False, host='0.0.0.0')
