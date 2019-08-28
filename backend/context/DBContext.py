# -*- coding=utf-8 -*-
'''
 * @Author: GyDi
 * @Modified: 2019-8-25
 * @Description: 提供数据库访问的接口
'''

from os.path import dirname, abspath, join
import sqlite3

DB_NAME = "data.db"
MIN_DB_NAME = "min_data.db"
DB_PATH = join(dirname(dirname(abspath(__file__))), 'database', MIN_DB_NAME)


class DBContext():
    _current_path = DB_PATH
    _error = False

    def __enter__(self):
        self.conn = sqlite3.connect(self._current_path)
        self.cursor = self.conn.cursor()
        return self

    def get_connection(self):
        return self.conn

    def get_cursor(self):
        return self.cursor

    def is_error(self):
        return self._error

    def exec(self, sqlstr, args=None):
        '''
        只负责执行sql语句, 返回是否执行成功
        '''
        try:
            if args:
                self.cursor.execute(sqlstr, args)
            else:
                self.cursor.execute(sqlstr)
        except Exception as e:
            print("DBContext Error: ", e)
            self._error = True
            return False
        return True

    def execmany(self, sqlstr, vals):
        try:
            self.conn.executemany(sqlstr, vals)
        except Exception as e:
            print("DBContext Error: ", e)
            self._error = True
            return False
        return True

    def __exit__(self, exc_type, exc_value, traceback):
        #self.cursor.close()
        if exc_type:
            self._error = True
        else:
            self.conn.commit()
        self.conn.close()


'''
可以直接使用with来操作

with dbcontext() as dh:
    dh.get_cursor().execute(...)

'''
