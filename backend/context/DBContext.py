# -*- coding=utf-8 -*-
'''
 * @Author: GyDi
 * @Modified: 2019-9-4
 * @Description: 提供mysql数据库访问的接口
'''
from context import get_db
import pymysql


class DBContext():
    _error = False

    def __init__(self):
        # type指明游标的类型为字典类型
        self.conn = get_db()

    def __enter__(self):
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        return self

    def get_cursor(self):
        return self.cursor

    def is_error(self):
        return self._error

    def exec(self, sqlstr, args=()):
        num = 0
        try:
            num = self.cursor.execute(sqlstr, args)
        except Exception as e:
            print("DBContext Error:", e)
            self._error = True
        return num

    def execmany(self, sqlstr, vals):
        try:
            self.conn.executemany(sqlstr, vals)
        except Exception as e:
            print("DBContext Error: ", e)
            self._error = True
            return False
        return True

    def fetchone(self):
        return self.cursor.fetchone() if not self._error else None
    
    def fetchall(self):
        return self.cursor.fetchall() if not self._error else None

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type or self._error:
            self._error = True
            self.conn.rollback()
        else:
            self.conn.commit()
        self.cursor.close()
        # self.conn.close()


'''
可以直接使用with来操作

with dbcontext() as dh:
    dh.get_cursor().execute(...)

'''
