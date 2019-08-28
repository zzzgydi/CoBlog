# -*- coding=utf-8 -*-
'''
@Author: GyDi
@Description: this script is used to create the database
'''

from DBContext import DBContext

sql_note = '''
    create table note(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        label varchar(256),
        title text,
        content text,
        modified varchar(128),
        state varchar(64)
    );
'''


if __name__ == "__main__":
    with DBContext() as d:
        d.get_cursor().execute(sql_note)
    # pass
    print("已经初始化了")
