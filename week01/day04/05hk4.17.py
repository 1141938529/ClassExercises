# /习题4.17
import random


# 游戏获胜的规则  1 代表num1胜  0 代表平局 -1 代表num2胜
def victory(num1, num2):
    if (num1 == 0):
        if (num2 == 1):
            return -1;
        elif (num2 == 0):
            return 0
        else:
            return 1
        pass
    elif (num1 == 1):
        if (num2 == 0):
            return 1
            pass
        elif (num2 == 1):
            return 0
            pass
        else:
            return -1
            pass
    else:
        if (num2 == 0):
            return -1
            pass
        elif (num2 == 1):
            return 1
            pass
        else:
            return 0
            pass


# 0---paper  1--rock  2--scissors
def isRPS(num):
    if num == 0:
        return "scissor"
        pass
    elif num == 1:
        return "rock"
    else:
        return "paper"
    pass


computerRps = random.randint(0, 2)
userRps = eval(input("scissor(0),rock(1),paper(2)："))
if (victory(computerRps, userRps) == 1):
    print("the computer is %s.You are %s.Computer won." % (isRPS(computerRps), isRPS(userRps)))
    pass
elif (victory(computerRps, userRps) == 0):
    print("the computer is %s.You are %s.it is a draw." % (isRPS(computerRps), isRPS(userRps)))
    pass
else:
    print("the computer is %s.You are %s.You won." % (isRPS(computerRps), isRPS(userRps)))
    pass
