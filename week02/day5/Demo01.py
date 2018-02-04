import os


def onlyread():
    file = open("./myTest/hello.txt", "r", encoding="utf-8")
    print(file.read())
    file.close()


def onlyWrite():
    file = open("./myTest/hello1.txt", "w", encoding="utf-8")
    # 返回值为 字符个数
    file.write("hello,python! I'm  coming ")
    file.close()

def addmodel():
    file = open("./mytest/hello1.txt", "a", encoding="utf-8")
    file.write("\n hello  world  my name is cfw")
    file.close()


def wbMethom():
    # os.mkdir("./mytest2")
    # os.remove("./mytest2/test.txt")
    file = open("./mytest2/test.txt", "wb")
    file.write(b"I love lisa,forever ~~~!")
    file.close()

file = open("./mytest2/test2","a+",encoding="utf-8")
# file.write("\n床前明月光，\n凝视地上霜。\n举头望明月，\n低头思故乡。")
# file.write("\n    by李白")
file.seek(0)
print(file.readline())
print(file.readline())
# for item in file:
#     print(file.readline(),end="")
# mlist = file.readlines()
# for item in mlist:
#     print(item,end="")
file.close()


# wbMethom()
# addmodel()
# onlyread()
# onlyWrite()
