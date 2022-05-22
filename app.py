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
    response = {"error": True}
    if request.method == "POST":
        data = json.loads(request.get_data(as_text=True))

        if data['state'] == 0:
            state, o_email, o_user, desc = accountOpr.sign_in(data['account'], data['passwd'])
            if state == 1:
                response["error"] = False
            response["desc"] = desc
            response["email"] = o_email
            response["userName"] = o_user

        elif data['state'] == 1:
            state, desc = accountOpr.sign_up(data['email'], data['username'], data['passwd'])
            if state == 1:
                response["error"] = False
            response["desc"] = desc
            response["email"] = data['email']
            response["userName"] = data['passwd']
        else:
            print(data['state'])
            response["desc"] = "Invalid request status"
    else:
        response["desc"] = request.method

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

