#! C:\Python36\python.exe
# coding:utf-8
from cgi import FieldStorage

fs = FieldStorage()
user = fs.getvalue("user")
pwd = fs.getvalue("pwd")

print("user:"+user+",pwd:"+pwd)