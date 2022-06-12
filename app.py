# -*- coding: utf-8 -*-
# @Time    : 2022/5/21-16:09
# @Author  : FreanJa L
# @Email   : root@freanja.cn
# @File    : app.py
# @Desc    :
import json
import random

from flask import Flask
from flask import Flask
from flask import request
from flask import render_template
from flask import Response
from flask import jsonify
import sql_server
import accountOpr
import postOpr

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
    account = {"userId": -1, "email": "", "userName": "", "password": "", "photo": ""}
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
            photo = str(random.randint(1, 105))
            account = {"userId": -1, "email": data['email'], "userName": data["username"], "password": data["passwd"],
                       "photo": photo}
            state, account["userId"], desc = accountOpr.sign_up(data['email'], data['username'], data['passwd'], photo)
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


@app.route("/fetchPosts", methods=["GET"])
def fetch_posts():
    info = {"error": True, "desc": ""}
    state, count, postList, desc = postOpr.get_all_post()
    if state == 1:
        info["error"] = False
    info["desc"] = desc
    response = {"postList": postList, "count": count, "info": [info]}

    for post in response["postList"]:
        print(post)

    return jsonify(response)


@app.route("/fetchComments", methods=["POST"])
def fetch_comments():
    data = json.loads(request.get_data(as_text=True))

    info = {"error": True, "desc": ""}
    state, count, comments, desc = postOpr.get_all_comments(data['postId'])
    if state == 1:
        info["error"] = False
    info["desc"] = desc
    response = {"comments": comments, "count": count, "info": [info]}

    for post in response["comments"]:
        print(post)

    return jsonify(response)


@app.route("/createComment", methods=["POST"])
def create_comment():
    data = json.loads(request.get_data(as_text=True))

    info = {"error": True, "desc": ""}
    state, count, comments, desc = postOpr.create_comment(data['postId'], data['userId'], data['comment'])
    if state == 1:
        info["error"] = False
    info["desc"] = desc
    response = {"comments": comments, "count": count, "info": [info]}

    for post in response["comments"]:
        print(post)

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')



















