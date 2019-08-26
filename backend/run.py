# -*- coding=utf-8 -*-
from datetime import timedelta
from flask import Flask, request, render_template, jsonify
# from backend.facade import FileSys, MsgSys, UserSys
from model.Result import Result
from controller import UserController
app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")


app.config['SECRET_KEY'] = "BBT1234567890GYDIBBTV2_0"
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=3)

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
# 	return render_template("index.html")



@app.route('/test')
def test_all():
    res = Result(1, a=10, b=[1,1,2,2], c='hhh')
    return jsonify(res.toDict())

app.add_url_rule('/api/login', view_func=UserController.login, methods=['POST'])
app.add_url_rule('/api/register', view_func=UserController.register, methods=['POST'])


if __name__ =="__main__":
	app.run(debug=False, host='0.0.0.0')
