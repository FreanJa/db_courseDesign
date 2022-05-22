# -*- coding: utf-8 -*-
# @Time    : 2022/5/22-00:35
# @Author  : FreanJa L
# @Email   : root@freanja.cn
# @File    : my_sql.py
# @Desc    :
import pymysql


class MySql:
    def __init__(self):
        self.db = pymysql.connect(
            # host='122.51.176.43',  # 服务器IP
            host='127.0.0.1',  # 服务器IP
            user='root',  # 用户名
            passwd='admin123',  # 密码
            db='db_course_design',  # 数据库名字
            charset='utf8',  # 字符集
        )

        self.cur = self.db.cursor()

    # 获取查询条数
    def get_count(self, sql):
        count = self.cur.execute(sql)
        return count

    # 获取查询的第一条数据
    def get_first_data(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    # 获取查询的多条数据
    def get_mult_data(self, sql, size=None):
        self.cur.execute(sql)
        if size:
            return self.cur.fetchmany(size)
        else:
            return self.cur.fetchall()

    # 插入语句
    def insert(self, sql):
        insert = self.cur.execute(sql)
        print("受影响行数:%d" % insert)
        self.db.commit()
        return insert

    # 关闭连接
    def close_db(self):
        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    db = MySql()
    sql = "select * from userAccount"
    result = db.get_mult_data(sql)
    print(result)
    db.close_db()
