# 习题4.3
import random

a, b, c, d, e, f = eval(input("enter a,b,c,d,e,f:"))
ad_bc = a * d - b * c
if not ad_bc:
    print("The equation has no solution")
else:
    x = (e * d - b * f) / ad_bc
    y = (a * f - e * c) / ad_bc
    print("x is %f and y is %f" % (x, y))
    pass
# 习题4.4

r1 = random.randint(0, 100)
r2 = random.randint(0, 100)
sum1 = eval(input("请输入%d和%d这两个数的和为：" % (r1, r2)))
if sum1 == (r1 + r2):
    print("恭喜你，答对了")
    pass
else:
    print("很遗憾，答错了")
    pass
