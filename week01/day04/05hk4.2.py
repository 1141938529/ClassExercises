import random
a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
sum = eval(input("请输入%d，%d，%d三个数的和为："%(a,b,c)))
if sum==(a+b+c) :
    print("你算对了")
    pass
else:
    print("你算错了")
    pass