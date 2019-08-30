# -*- coding=utf-8 -*-
'''
@Author: GyDi
@Description: this script is used to create the database
'''

from DBContext import DBContext
#from backend.data.DBContext import DBContext


sql_user = '''
    create table user(
        id varchar(64) primary key not null,
        account varchar(128) not null,
        password varchar(128) not null,
        name varchar(128)
    );'''

sql_note = '''
    create table note(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author varchar(64) not null,
        label varchar(256),
        title text,
        content text,
        modified integer,
        state varchar(32)
    );'''

sql_tag = '''
    create table label(
        id integer primary key autoincrement,
        user varchar(64) not null,
        value varchar(256) not null,
        color varchar(256)
    );'''

# sql_book = '''
#     create table book(
#         id varchar(64) primary key not null,
#         name varchar(256),
#         visible varchar(32) not null,
#         creator varchar(64) not null,
#         created varchar(128) not null,
#         desc text
#     ); '''

# sql_userbook = '''
#     create table userbook(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user varchar(64) not null,
#         book varchar(64) not null
#     ); '''

if __name__ == "__main__":
    with DBContext() as d:
        d.get_cursor().execute(sql_user)
        d.get_cursor().execute(sql_note)
        d.get_cursor().execute(sql_tag)
        # d.get_cursor().execute(sql_book)
        # d.get_cursor().execute(sql_userbook)
        pass
    print("已经初始化了")
