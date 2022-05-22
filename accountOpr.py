# -*- coding: utf-8 -*-
# @Time    : 2022/5/22-00:31
# @Author  : FreanJa L
# @Email   : root@freanja.cn
# @File    : accountOpr.py
# @Desc    :
import re
import my_sql


# 登陆
def sign_in(in_usr, in_passwd):
    flag = 1        # 1 - email
    db = my_sql.MySql()
    sql = "select * from userAccount where "
    if re.search('@', in_usr):
        sql = sql + "Email = " + "'" + in_usr + "'"
    else:
        flag = 0
        sql = sql + "userName = " + "'" + in_usr + "'"
    count = db.get_count(sql)
    if count == 0:
        db.close_db()
        if flag:
            return 0, in_usr, "", "Invalid account"
        else:
            return 0, "", in_usr, "Invalid account"
    result = db.get_first_data(sql)
    db.close_db()
    if result[3] == in_passwd:
        return 1, result[1], result[2], "success"
    else:
        if flag:
            return 0, in_usr, "", "Wrong password"
        else:
            return 0, "", in_usr, "Wrong password"


# 注册
# -2 未知错误   -1 - 重复email  0 - 重复用户名   1 - 注册成功
def sign_up(in_email, in_name, in_passwd):
    db = my_sql.MySql()
    sql = "select * from userAccount where "
    if db.get_count(sql + "email = '" + in_email + "'") != 0:
        return 0, "Duplicate Email"
    if db.get_count(sql + "userName = '" + in_name + "'") != 0:
        return 0, "Duplicate User Name"
    sql = "insert into userAccount (email,username,password) values ('" + \
          in_email + "','" + \
          in_name + "','" + \
          in_passwd + "');"
    print(sql)
    insert = db.insert(sql)
    if insert == 0:
        return 0, "Unknown error, please contact your administrator"
    print("insert success")
    return 1, "Successful registration, go to login!"


def test_sign_in():
    username = "freanja"
    email = "freanja.l@gmail.com"
    passwd = "123"
    state, e_mail, user, desc = sign_in(email, passwd)
    if state == 0:
        print("[Error] " + desc)
    else:
        print("👋 Welcome back " + user)


def test_sign_up():
    username = "freanja"
    email = "freanja.l@gmail.com"
    passwd = "123"
    state, desc = sign_up(email, username, passwd)
    if state == 0:
        print("[Error] " + desc)
    else:
        print(desc)


if __name__ == '__main__':
    test_sign_up()
