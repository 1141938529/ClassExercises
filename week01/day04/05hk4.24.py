import random

value = random.randint(1, 52)
value = 1
code = value % 13
pokerSuit = (value - 1) // 13


def isSuit(pokerSuit):
    if (pokerSuit == 0):
        str = "梅花"
    elif (pokerSuit == 1):
        str = "红桃"
    elif (pokerSuit == 2):
        str = "黑桃"
    elif (pokerSuit == 3):
        str = "方块"
    return str

def isCode(code):
    if (code == 0):
        str = "K"
    elif (code == 1):
        str = "A"
    elif (code == 2):
        str = "2"
    elif (code == 3):
        str = "3"
    elif (code == 4):
        str = "4"
    elif (code == 5):
        str = "5"
    elif (code == 6):
        str = "6"
    elif (code == 7):
        str = "7"
    elif (code == 8):
        str = "8"
    elif (code == 9):
        str = "9"
    elif (code == 10):
        str = "10"
    elif (code == 11):
        str = "J"
    elif (code == 12):
        str = "Q"
    return str
    pass

print("这张牌为%s%s"%(isSuit(pokerSuit),isCode(code)))