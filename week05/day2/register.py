#! C:\Python36\python.exe
# coding:utf-8
import html
from cgi import FieldStorage
import re

print("Content-type:text/html")
print()

fs = FieldStorage()
user = fs.getvalue("user")
pwd = fs.getvalue("pwd")

def userIsok():
    if len(user) >= 6 and len(user) <= 20:
        for char in user:
            if (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
                continue
            else:
                print(char)
                print("用户名输入有误，请确认为英文字母")
                return False
    else:
        print("用户名输入有误,长度在6-20之间")
        return False
    return True

def pwdIsok():
    if len(pwd) >= 6 and len(pwd) <= 20:
        for char in pwd:
            if char.isdigit():
                continue
            else:
                print(char)
                print("密码有误，请确认为数字")
                return False
    else:
        print("密码输入有误,长度在6-20之间")
        return False
    return True

print('''
<head>
    <meta charset="gbk">
    <title>登录界面</title>
    <style>
    </style>
</head>
<body>
''')
if userIsok() and pwdIsok():
    print("用户注册成功")
    print("欢迎加入,<h3>%s先生</h3>"%user)
else:
    pass

print("</body>")

