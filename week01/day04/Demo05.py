
# 2000年是龙年 输入任意年份 判断生肖

years = eval(input("请输入你的年份："))
year = (years-2000)%12
if year>=0 :
     pass
else:
    year+= 12
if(year == 0):
    print("%d年是龙年"%years)
    pass
elif(year==1):
    print("%d年是蛇年"%years)
    pass
elif(year==2):
    print("%d年是马年" % years)
    pass
elif(year==3):
    print("%d年是羊年" % years)
    pass
elif(year==4):
    print("%d年是猴年" % years)
    pass
elif(year==5):
    print("%d年是鸡年" % years)
    pass
elif(year==6):
    print("%d年是狗年" % years)
    pass
elif(year==7):
    print("%d年是猪年" % years)
    pass
elif(year==8):
    print("%d年是鼠年" % years)
    pass
elif(year==9):
    print("%d年是牛年" % years)
    pass
elif(year==10):
    print("%d年是虎年" % years)
    pass
elif(year==11):
    print("%d年是兔年" % years)
    pass


