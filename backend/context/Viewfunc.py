# -*- coding=utf-8 -*-

from controller import QiniuConfig, UserController, NoteController


# 视图函数定义
ViewFuncs = {
    '/api/login': UserController.login,
    '/api/register': UserController.register,
    '/api/check': UserController.check,
    '/api/logout': UserController.logout,
    '/api/setpwd': UserController.set_password,
    '/api/setname': UserController.set_name,
    '/api/addnote': NoteController.add_note,
    '/api/getnotes': NoteController.get_allnotes,
    '/api/usernotes': NoteController.get_usernotes,
    '/api/viewnote': NoteController.view_note,
    '/api/updatenote': NoteController.update_note,
    '/api/notestate': NoteController.revise_state,
    '/api/delnote': NoteController.delete_note,
    '/api/addlabel': NoteController.add_label,
    '/api/getlabels': NoteController.get_labels,
    '/api/gettoken': QiniuConfig.get_token,
}

'''
app.add_url_rule('/api/login', view_func=UserController.login, methods=['POST'])
app.add_url_rule('/api/register', view_func=UserController.register, methods=['POST'])
app.add_url_rule('/api/check', view_func=UserController.check, methods=['POST'])    # 检查登录是否有效
app.add_url_rule('/api/logout', view_func=UserController.logout, methods=['POST'])
app.add_url_rule('/api/setpwd', view_func=UserController.set_password, methods=['POST'])
app.add_url_rule('/api/setname', view_func=UserController.set_name, methods=['POST'])

app.add_url_rule('/api/addnote', view_func=NoteController.add_note, methods=['POST'])
app.add_url_rule('/api/getnotes', view_func=NoteController.get_allnotes, methods=['POST'])  # 首页获取
app.add_url_rule('/api/usernotes', view_func=NoteController.get_usernotes, methods=['POST']) # 用户页获取
app.add_url_rule('/api/viewnote', view_func=NoteController.view_note, methods=['POST'])
app.add_url_rule('/api/updatenote', view_func=NoteController.update_note, methods=['POST'])
app.add_url_rule('/api/notestate', view_func=NoteController.revise_state, methods=['POST'])
app.add_url_rule('/api/delnote', view_func=NoteController.delete_note, methods=['POST'])
app.add_url_rule('/api/addlabel', view_func=NoteController.add_label, methods=['POST'])
app.add_url_rule('/api/getlabels', view_func=NoteController.get_labels, methods=['POST'])

app.add_url_rule('/api/gettoken', view_func=QiniuConfig.get_token, methods=['POST'])
'''
