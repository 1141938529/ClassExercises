# 打印表格
import math

print(format("a", "<8s"), end=(""))
print(format("b", "<8s"), end=(""))
print("a ** b")
for i in range(5):
    print(format(i+1,"<8d"),end=(""))
    print(format(i + 2, "<8d"),end=(""))
    print(format((i+1)**(i+2), "<8d"))

#  2.13 分割数字
value = eval(input("enter an integer:"))
qian = value//1000
bai = (value-qian*1000)//100
shi = (value-qian*1000-bai*100)//10
ge = (value-qian*1000-bai*100-shi*10)
print(ge)
print(shi)
print(bai)
print(qian)

# 三角形的面积
x1,y1,x2,y2,x3,y3 = eval(input("enter three points for a"
                         " triangle:") )
def Sidess(x1,y1,x2,y2):
    sides = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return sides
s1 = Sidess(x1,y1,x2,y2)
s2 = Sidess(x3,y3,x2,y2)
s3= Sidess(x1,y1,x3,y3)
s=(s1+s2+s3)/2
area =math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

print("the area is ",format(area,".1f"))





