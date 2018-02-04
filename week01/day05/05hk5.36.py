# 0--代表剪刀 1--代表石头 2--代表布
import random

RPGList = ["剪刀", "石头", "布"]
# 统计电脑和人连续获胜的次数
count1 = 0
count2 = 0


# 获胜规则： 1代表num1 获胜   0代表平局  -1代表num2 获胜
def VictorRuler(num1, num2):
    if ((num1 - num2) > 0 or (num1 - num2) == -2):

        return 1
    elif (num1 == num2):
        return 0
    else:
        return -1


while True:
    computerNum = random.randint(0, 2)
    userNum = eval(input("请选择你要出的（0--代表剪刀 1--代表石头 2--代表布）："))
    print("你出的是：%s，电脑是%s" % (RPGList[userNum], RPGList[computerNum]), end=" ")

    currNum = VictorRuler(userNum, computerNum)
    if currNum == 1:
        count1 += 1
        count2 = 0
        # print(conut1)
        print("你赢了！")
    elif currNum == -1:
        count2 += 1
        count1 = 0
        # print("count1=%d  conut2=%d" % (count1, count2))
        print("电脑赢了！")
    else:
        print("平局！")
        count1 = 0
        count2 = 0
    # 判断是否胜利
    if (count1 == 2):
        print("恭喜你！最终获胜")
        print("game over")
        break
    if (count2 == 2):
        print("很遗憾！电脑最终获胜")
        print("game over")
        break
