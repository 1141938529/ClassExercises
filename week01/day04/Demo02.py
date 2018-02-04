# else if  语句
import random

look = random.randint(0,100)
print("你出生了，你的颜值为：%d"%(look))
if look>90 :
    print("恭喜你，你的颜值逆天了")
    pass
elif look>60:
    print("你的颜值还阔以")
    pass
else:
    print("呵呵哒，你咋出来的呢")
    pass

