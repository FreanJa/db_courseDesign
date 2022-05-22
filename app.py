# -*- coding: utf-8 -*-
# @Time    : 2022/5/21-16:09
# @Author  : FreanJa L
# @Email   : root@freanja.cn
# @File    : app.py
# @Desc    :
import json

from flask import Flask
from flask import Flask
from flask import request
from flask import render_template
from flask import Response
from flask import jsonify
import sql_server
import accountOpr

app = Flask(__name__)


@app.route('/')
def post():
    print(sql_server.search_template())
    return sql_server.search_template()


@app.route("/create", methods=['POST', "GET"])
def create():
    if request.method == 'POST':
        print("post")
        data = json.loads(request.get_data(as_text=True))
        print(data)
        # for key, value in data:
        #     print(key, value)

        user_info = {
            'user': request.json['user'],
            'passwd': request.json['passwd']
        }
        print(user_info)
        return jsonify(user_info)
    else:
        print("Not POST")
        print(request.method)
        return "Error"


# 0 - signIn    1 - signUp
@app.route("/user", methods=["POST", "GET"])
def user():
    print(request.method)
    info = {"error": True, "desc": ""}
    account = {"email": "", "userName": ""}
    if request.method == "POST":
        data = json.loads(request.get_data(as_text=True))

        # 登陆
        if data['state'] == 0:
            state, account, desc = accountOpr.sign_in(data['account'], data['passwd'])
            if state == 1:
                info["error"] = False
            info["desc"] = desc

        # 注册
        elif data['state'] == 1:
            account = {"email": data['email'], "userName": data["username"]}
            state, desc = accountOpr.sign_up(data['email'], data['username'], data['passwd'])
            if state == 1:
                info["error"] = False
            info["desc"] = desc

        # 未知错误
        else:
            print(data['state'])
            info["desc"] = "Invalid request status"
    else:
        info["desc"] = request.method

    response = {"account": [account], "info": [info]}
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

