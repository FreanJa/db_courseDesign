# -*- coding: utf-8 -*-
# @Time    : 2022/6/12-04:06
# @Author  : FreanJa L
# @Email   : root@freanja.cn
# @File    : postOpr.py.py
# @Desc    :
import time

import my_sql


# 返回所有帖子
def get_user_info(id):
    db = my_sql.MySql()
    sql = "select * from userAccount where uuid = '" + str(id) + "';"

    count = db.get_count(sql)

    if count == 0:
        db.close_db()
        return "佚名", "60"

    result = db.get_first_data(sql)
    db.close_db()

    return result[2], str(result[4])


def get_all_post():
    postList = {}
    db = my_sql.MySql()
    sql = "select * from posts"

    count = db.get_count(sql)

    if count == 0:
        db.close_db()
        return 0, 0, postList, "No posts."

    result = db.get_mult_data(sql)
    db.close_db()

    posts = []
    for row in result:
        wn, wp = get_user_info(row[4])
        post = {"postId": row[0], "title": row[1], "subTitle": row[2], "time": row[3], "writerId": row[4],
                "writerName": wn, "writerPhoto": wp, "text": row[5], "imgCount": row[6]}
        posts.append(post)

    # postList["posts"] = posts
    # for post in postList["posts"]:
    #     print(post)

    return 1, count, posts, "success"


def get_all_comments(id):
    commentList = {}

    db = my_sql.MySql()
    sql = "select * from comments where postId = '" + str(id) + "';"

    count = db.get_count(sql)

    if count == 0:
        db.close_db()
        return 0, 0, commentList, "No comment."

    result = db.get_mult_data(sql)
    db.close_db()

    comments = []
    for row in result:
        un, up = get_user_info(row[2])
        comment = {"commentsId": row[0], "postId": row[1], "userId": row[2], "userName": un, "userPhoto": up,
                   "time": row[3], "text": row[4]}
        comments.append(comment)

    return 1, count, comments, "success"


def create_comment(postId, userId, comment):
    db = my_sql.MySql()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "insert into comments (postId, userId, time, text) values (" + \
          str(postId) + "," + \
          str(userId) + ",'" + \
          current_time + "','" + \
          comment + "');"
    print(sql)
    insert = db.insert(sql)
    if insert == 0:
        return 0, 0, {}, "Unknown error, please contact your administrator"

    return get_all_comments(postId)


if __name__ == '__main__':
    # error, posts, desc = get_all_post()
    # create_comment(12, 3, "asasdadasd")
    pass


