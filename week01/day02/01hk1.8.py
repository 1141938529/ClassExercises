import math


# 习题1.8 求圆的面积和周长
def AreaPeriCir(radius):
    area = radius * radius * math.pi
    peri = radius * 2 * math.pi
    print("半径是", radius, "的圆周长为", format(peri, ".2f"), "，面积为", format(area, ".2f"))


# 习题1.9 求矩形的面积和周长
AreaPeriCir(5.5)


def AreaPeri2(width, height):
    area = width * height
    peri = (width + height) * 2

    print("长是", width, "宽是", height, "的矩形周长为", format(peri, ".2f"), "，面积为", format(area, ".2f"))


AreaPeri2(4.5, 7.9)
# 习题1.10  求平均速度
perSpeed = (14 / 1.6) / ((45 + 30 / 60) / 60)
print(perSpeed)


# 习题1.11 求未来5年的人口数
def nPeople(n):
    people = 3120324986
    sencondsOfYear = 360 * 24 * 60 * 60
    for i in range(n):
        people = people + sencondsOfYear // 7 - sencondsOfYear // 13 + sencondsOfYear // 45
        print("接下来的第", n + 1, "年人口为", people)


nPeople(5)
