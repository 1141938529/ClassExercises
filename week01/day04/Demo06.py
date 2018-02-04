# 随机生成一个两位数中奖码  用户输入一个两位数字
# 如果全等于 为特等奖
# 数字相同为 大奖 有一个数字相同 安慰奖  佛则没有奖励
import random

winnerCode = random.randint(10, 99)
customerCode = eval(input("请输入一个2位数的号码："))
winnerCodeX = winnerCode // 10
winnerCodeY = winnerCode % 10
customerCodeX = customerCode // 10
customerCodeY = customerCode % 10
print("你好，今日中奖号码为:%d"%winnerCode)
if winnerCode == customerCode:
    print("୧(๑•̀◡•́๑)૭恭喜你，你中了特等奖")
    pass
elif ((winnerCodeX) == (customerCodeY) and (winnerCodeY) == (customerCodeX)):  # 判断
    print("୧(๑•̀◡•́๑)૭恭喜你，你中了大奖")
    pass
elif (winnerCodeX == customerCodeX or winnerCodeX == customerCodeY
      or winnerCodeY == customerCodeY or winnerCodeY == customerCodeX):
    print("୧(๑•̀◡•́๑)૭  恭喜你，你中了安慰奖")
    pass
else:
    print('''o(╥﹏╥)o 很遗憾，你没能中奖.
            ❤❤祝你下次好运！❤❤''')
    pass
print("a">='2')