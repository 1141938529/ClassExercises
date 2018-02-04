#! C:\Python36\python.exe
# coding:utf-8

# ·显示记者张三的全部文章信息()：http://localhost/cgi-bin/showArticle.py?author=张三
from cgi import FieldStorage

import pymysql

print("Content-type:text/plain")
print()


print("Content-type:text/plain")
print()


def selectArticle(name):
    mstr = "%"+name+"%"
    try:
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="mynews", charset="utf8")
        cursor = conn.cursor()
        cursor.execute(
            "select * from t_article JOIN t_author ON t_article.author_id = t_author.id WHERE t_author.name like'%s'"%(mstr))
        res = cursor.fetchall()
        print(name+"的文章有：")
        if not(len(res) ==0):
            for i in range(len(res)):
                article = res[i]
                print(str(i + 1) + "." + article[1] + " 时间为：" + article[2])
        else:
            print("没能找到文章！")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    fs = FieldStorage()
    name = fs.getvalue("author")

    selectArticle(name)

    pass