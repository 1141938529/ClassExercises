class Point():
    __pointX = 0
    __pointY = 0

    def __init__(self, pointX=0, pointY=0):
        self.__pointX = pointX
        self.__pointY = pointY

    def getPointX(self):
        return self.__pointX

    def getPointY(self):
        return self.__pointY

    def distance(self, p1):
        return ((self.__pointX - p1.getPointX()) ** 2 + (self.__pointY - p1.getPointY()) ** 2) ** (1 / 2)

    def isNearBy(self, p1):
        if self.distance(p1) < 5:
            return True
        else:
            return False

if __name__ =="__main__":
    x1,y1,x2,y2 = eval(input("请输入两个点的坐标："))
    p1= Point(x1,y1)
    p2= Point(x2,y2)
    print("这两点的距离为：",format(p1.distance(p2),".2f"))
    print("这两点距离是否很近？" ,p1.isNearBy(p2))

