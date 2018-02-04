# 习题4.15
# 中奖问题 三位数
# 完全匹配10000美金  匹配数字 3000美金  匹配一个数字 1000美金
import random

lotteryNo = random.randint(0, 1000)
winnerNo = eval(input("请输入你的中奖号码："))
lotteryNo01 = lotteryNo // 100
lotteryNo02 = (lotteryNo % 100) // 10
lotteryNo03 = lotteryNo % 10
winnerNo01 = winnerNo // 100
winnerNo02 = (winnerNo % 100) // 10
winnerNo03 = winnerNo % 10
print("中奖号码为：", lotteryNo)

# def isEqual(a, b, c, d, e, f):
#     if (a == d):  # a=d
#         if (b == e):  # a=d b=e
#             return False
#             pass
#         elif (b == f):  # a=d  b=f
#             if (c == e):  # a=d  b=f c==e
#                 return True
#             else:
#                 return False
#             pass
#         else:  # a=f  b!=e!=f
#             return False
#             pass
#     elif (a == e):
#         pass
#     elif (a == f):
#         pass
#     else:
#         return False

pass
if lotteryNo == winnerNo:
    print("恭喜你获得奖金10000美元")
    pass

elif \
        ((lotteryNo01 == winnerNo01 and lotteryNo02 == winnerNo03 and lotteryNo03 == winnerNo02)
         or (lotteryNo01 == winnerNo02 and lotteryNo02 == winnerNo03 and lotteryNo03 == winnerNo01)
         or (lotteryNo01 == winnerNo02 and lotteryNo02 == winnerNo01 and lotteryNo03 == winnerNo03)
         or (lotteryNo01 == winnerNo03 and lotteryNo02 == winnerNo02 and lotteryNo03 == winnerNo01)
         or (lotteryNo01 == winnerNo03 and lotteryNo02 == winnerNo01 and lotteryNo03 == winnerNo02)
         ):

    print("恭喜你获得奖金3000美元")
    pass
elif \
        ((lotteryNo01 == winnerNo01) or (lotteryNo01 == winnerNo02) or (lotteryNo01 == winnerNo03)
         or (lotteryNo02 == winnerNo01) or (lotteryNo02 == winnerNo02) or (lotteryNo02 == winnerNo03)
         or (lotteryNo03 == winnerNo01) or (lotteryNo03 == winnerNo02) or (lotteryNo03 == winnerNo03)
         ):

    print("恭喜你获得奖金1000美元")
    pass
else:

    print("很遗憾！ 你没能中奖！")
    pass
