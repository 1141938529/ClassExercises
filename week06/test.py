import os
import re
#
# reStockName='\w+\((\d{6})\)'
# reStockName = re.compile(reStockName)
#
# print(re.search(reStockName,'0512R028(203041)').group(1))


# class myTest():
#     @staticmethod
#     def test():
#         pass

# def sayHello(name, age=20, *args, **kwargs):
#     print(name, age, args, kwargs)
# # 函数调用
# sayHello("fuck", 30, 40, 50, sex="男", gay=True)

class MyException(Exception):
    def __init__(self):
        super().__init__()

    def handleError(self):
        print("密码长度应为6-12位字符！")

    pass


def register():
    print("****欢迎来到注册页面****")
    name = input("请输入昵称：")
    while True:
        try:
            pwd = input("请输入密码：")
            if len(pwd) < 6 or len(pwd) > 12:
                raise MyException()
            else:
                break
        except MyException as e:
            e.handleError()
            print("请重新输入！")
    print("注册成功！")
    pass


def findFiles ():
    filePath = input("请输入文件夹路径：")
    if os.path.exists(filePath):
        print("ok")
        pass
    else:
        print("输入的路径不存在！")


if __name__ == '__main__':
    # register()
    findFiles()


