from myfile.ASCIICodeGenerator import ASCIICodeNumber,RandomCapitalletters,RandomLowercaseletters,RandomNumber
from myfile.BHDConverter import BHDConverter
def HomeWork1():
    print("随机获取一个小写字母：%s"%(RandomLowercaseletters()))
    print("随机获取大写字母：%s"%(RandomCapitalletters()))
    print("随机获取数字字符：%s"%(RandomNumber()))
    print("随机获取ASCII字符：%s"%(ASCIICodeNumber()))
def HomeWork002():
    num = eval(input("请输入一个十进制数："))
    num2 = BHDConverter(num)
    print("%d转换成十六进制为：%s"%(num,num2))

HomeWork002()

