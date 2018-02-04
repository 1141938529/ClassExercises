import re

import pymysql
import requests

'''
. 任意从网上拿5篇新闻，提取其中的媒体信息(名字、)、作者、日期、邮箱、网址
·将提取到的信息存入数据库的对应表：
    文章表（自增长主键ID，标题，日期，媒体，外键作者ID）
    记者表（自增长ID，邮箱、媒体单位）
·显示记者张三的全部文章信息：http://localhost/articles?author=张三

'''
from week05.homework.myNews import MynewsClass

urlList = {
    "http://news.163.com/17/1030/10/D206RPMV000189FH.html",
    "http://news.163.com/17/1030/08/D200FTTP0001899N.html",
    "http://news.163.com/17/1030/19/D216I5870001875O.html",
    "http://news.163.com/17/1030/18/D211HST00001875O.html",
    "http://news.163.com/17/1030/18/D2120N7R00018AOR.html"
}
'''
来源: <a id="ne_article_source" href="http://news.haiwainet.c
n/n/2017/1030/c3541093-31162908.html" target="_blank" rel="nofollow">海外网</a>
'''
# 媒体的正则表达式
reMedia = '来源:\s*<a.*?>(\w+)</a>'
reMedia = re.compile(reMedia)

# 标题的正则表达式
reTitle = '<h1.*>(.*)</h1>'
reTitle = re.compile(reTitle)

# 作者的正则表达式
reAuthor = '<span.*>责任编辑：\s*(\w+)</span>'
reAuthor = re.compile(reAuthor)
# 日期的正则表达式
reDate = '(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+来源:'
reDate = re.compile(reDate)
# 邮箱的正则表达式
reEmail = '\w+@\w+\.\w+\.?\w*'
reEmail = re.compile(reEmail)


# 将myNews存入数据库、
def saveDataToDB(myNews):
    try:
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="mynews", charset="utf8")
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO t_media(NAME) VALUES ('%s')" % (myNews.media))
            conn.commit()
        except Exception as e:
            print(e)

        try:
            cursor.execute("select id from t_media where name='%s'" % (myNews.media))
            media_id = cursor.fetchone()[0]
            print(media_id,type(media_id))
            cursor.execute("INSERT INTO t_author(NAME,media_id) VALUES('%s',%d)" % (myNews.author, media_id))
            conn.commit()
        except Exception as e:
            print(e)
            pass

        try:
            cursor.execute("select id from t_author where name='%s'" % (myNews.author))
            author_id = cursor.fetchone()[0]
            cursor.execute(
                "INSERT INTO t_article(NAME,date,author_id) VALUES('%s','%s',%d)" % (myNews.title, myNews.date,author_id))
            conn.commit()
        except Exception as e:
            print(e)
            pass
    except Exception as e:
        print(e)
        pass
    finally:
        cursor.close()
        conn.close()

    pass


if __name__ == '__main__':
    for url in urlList:
        html = requests.get(url).text
        media = reMedia.search(html).group(1)
        title = reTitle.search(html).group(1)
        author = reAuthor.search(html).group(1)
        date = reDate.search(html).group(1)
        email = reEmail.findall(html)

        print(media, title, author, date, email, url)
        myNews = MynewsClass(media, title, author, date, email, url)
        saveDataToDB(myNews)
    pass
