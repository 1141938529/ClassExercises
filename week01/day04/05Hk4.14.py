# / 习题4.14 猜正反面
import random

answer = random.randint(0, 1)
myAnswer = eval(input("请输入你的想法，正面输入1，"
                      "反面输入0："))


def isTopOrbotton(value):
    if value == 1:
        str = '正面'
    else:
        str = '反面'
    return str


if (answer == myAnswer):
    print("硬币是", isTopOrbotton(answer), "你猜测的是",
          isTopOrbotton(myAnswer), "\n恭喜你，才对了！")
    pass
else:
    print("硬币是", isTopOrbotton(answer), "你猜测的是",
          isTopOrbotton(myAnswer), "\n很遗憾，猜错了！")
    pass
