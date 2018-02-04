# 编写一个程序将某个指定字符串从一个文本文件中所有出现过的地方删除
# 输入提示一个文件名 和要删除的字符串
filename = input("enter a filename:")
rmstr = input("enter the string to be removed:")

file = open("./alldirs/"+filename,"a+",encoding="utf-8")
file.seek(0)
oldstr = file.read()
newstr = oldstr.replace(rmstr,"")
file.close()
file= open("./alldirs/"+filename,"w+",encoding="utf-8")
file.write(newstr)
file.close()
