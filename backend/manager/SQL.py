# -*- coding=utf-8 -*-
'''
@Author: GyDi
@Description:  存放有关用户的 sql语句
'''

sql_check_acct = '''
    select * from user
    where account=?;
    '''

sql_check_login = '''
    select * from user
    where account=? and password=?;
    '''

sql_add_user = '''
    insert into user(id, account, password, name)
    values (?,?,?,?);
    '''

sql_get_userinfo = '''
    select * from user
    where id=?;
    '''

sql_set_name = '''
    update user set name=?
    where id=?;
    '''

key_user = ('id', 'account', 'password', 'name')
key_note = ('id', 'bookid', 'label', 'title', 'content', 'modified', 'user', 'state')
key_book = ('id', 'name', 'visible', 'creator', 'created', 'desc')
key_userbook = ('id', 'user', 'book')


# book
sql_add_book = '''
    insert into book(id, name, visible, creator, created, desc)
    values(?,?,?,?,?,?);
    '''

sql_add_bookuser = '''
    insert into userbook(user, book)
    values(?, ?);
    '''

# 找到某书的创建者
sql_find_creator = '''
    select creator from book
    where id=?;
    '''

sql_del_bookuser = '''
    delete from userbook
    where user=? and book=?;
    '''

sql_add_note = '''
    insert into note(bookid, label, title, content, modified, user, state)
    values(?,?,?,?,?,?,?);
    '''

sql_update_note = '''
    update note set label=?, title=?, content=?, modified=?, user=?, state=?
    where id=? and bookid=?;
    '''

sql_get_note = '''
    select * from note
    where id=? and bookid=?;
    '''