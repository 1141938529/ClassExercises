'''
·写出身份证号码、手机号、邮箱的正则表达式
·身份证号码规则：6位地区号码+8位日期号码+4位尾号，最后一位可以是X
·手机号规则：开头为13、15、17、18之一，后跟9位任意数字
·邮箱规则：【@和.】以外的字符必须为小写字母、数字、下划线，不能以下划线开头
....@QQ.com.cn
'''
import os
import re

# re1 = "[1-9]\d{5}((19\d{2})|(200\d)|(201[0-7]))(((0[13578])|(1[02]))((0[1-9])|([12][0-9])" \
#       "|(3[01]))|(((0[469])|(11))((0[1-9])|([12][0-9])|(31))|(02((0[1-9])|([1[0-9])|" \
#       "(2[0-9])))\d{3}[\dx]"
# re1 = re.compile(re1)
re2 = "1[3578]\d{9}"

re3 = "[a-z0-9][a-z0-9_]+@[a-z0-9_]+(\.[a-z0-9_]+)+"
re3 ="[a-z0-9][a-z0-9_]*@[a-z0-9_]*\.[a-z0-9_]*"


'''
    写一个函数，传入一个文件夹路径，实现递归遍历并统计该文件夹下的文件数量
'''
num =0
def findFiles(fileName):
    global num
    for item in os.listdir(fileName):
        if os.path.isfile(fileName+"/"+item):
            num +=1
        else:
            print(fileName+"/"+item)
            findFiles(fileName+"/"+item)
    return num
    pass

if __name__ == '__main__':
    # mstr1 = "36220419920721813x"
    # res = re1.search(mstr1)
    # print(res)
    # print(re.match(re3, "abc12345@qq.com.cn").group())

    flieList = []
    res = findFiles(r"F:/Python/其他文字资料")
    print(res)
    pass
