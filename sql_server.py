import pymysql
import json

from flask import jsonify

ipaddress = "122.51.176.43"
user = ""
passwd = ""
db = ""

myql = pymysql.connect(
    host='122.51.176.43',  # 服务器IP
    user='tmp2',  # 用户名
    passwd='123',  # 密码
    db='db_course_design',  # 数据库名字
    charset='utf8',  # 字符集
)


def search_template():
    cur = myql.cursor()
    sqlyj = "select*from testConn;"
    # sqlyi = "grant all privileges on *.* to tmp2@'%' identified by '123' with grant option;"
    # tmp = "flush privileges;"
    ret = cur.execute(sqlyj)
    dic = {}
    for row in cur.fetchall():
        # print(row)
        # dic[row[0]] = {'name': row[1], 'password': row[2], 'phone': row[3]}
        dic[row[1]] = row[2]

    print(dic)
    return jsonify(dic)


if __name__ == '__main__':
    search_template()

