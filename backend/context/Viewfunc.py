# -*- coding=utf-8 -*-

from controller import QiniuController, UserController, NoteController


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
    '/api/dellabel': NoteController.del_label,
    '/api/getlabels': NoteController.get_labels,
    '/api/gettoken': QiniuController.get_token,
    '/api/addurl': NoteController.add_url,
    '/api/delurl': NoteController.del_url,
    '/api/allurls': NoteController.all_url,
    '/api/geturl': NoteController.get_url,
    '/api/catalogue': NoteController.get_catalogue,
    '/api/looknote': NoteController.look_note
}
