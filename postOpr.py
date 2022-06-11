# -*- coding: utf-8 -*-
# @Time    : 2022/6/12-04:06
# @Author  : FreanJa L
# @Email   : root@freanja.cn
# @File    : postOpr.py.py
# @Desc    :
import my_sql


# 返回所有帖子
def get_all_post():
    postList = {"count": 0, "posts": []}
    db = my_sql.MySql()
    sql = "select * from posts"

    postList["count"] = db.get_count(sql)

    if postList["count"] == 0:
        db.close_db()
        return 0, postList, "No posts."

    result = db.get_mult_data(sql)
    db.close_db()

    posts = []
    for row in result:
        post = {"postId": row[0], "title": row[1], "subTitle": row[2], "time": row[3], "writeId": row[4], "text": row[5]}
        posts.append(post)

    postList["posts"] = posts
    for post in postList["posts"]:
        # print(postList["posts"][post]["title"] + "\t" + postList["posts"][post]["text"])
        print(post)

    return 1, postList, "success"


if __name__ == '__main__':
    error, posts, desc = get_all_post()
    print(posts)
    for post in posts:
        print(post)
