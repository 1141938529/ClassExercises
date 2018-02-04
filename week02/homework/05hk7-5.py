import math


class RegularPolygon():
    __n = 3
    __side = 1.0
    __x = 0.0
    __y = 0.0

    def __init__(self, n=3, side=1, x=0, y=0):
        self.__n = n
        self.__side = side
        self.__y = y
        self.__x = x
        pass

    def getN(self):
        return self.__n

    def getSide(self):
        return self.__side

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setN(self, n):
        self.__n = n

    def setside(self, side):
        self.__side = side

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getPerimeter(self):
        return self.__n * self.__side

    def getArea(self):
        return (self.__n * self.__side * self.__side) / (4 * math.tan(math.pi / self.__n))

    pass


if __name__ == "__main__":
    myrp1 = RegularPolygon()
    myrp2 = RegularPolygon(6,4)
    myrp3 = RegularPolygon(10,4,5.6,7.8)
    print(myrp1.getPerimeter(),myrp1.getArea())
    print(myrp2.getPerimeter(),myrp2.getArea())
    print(myrp3.getPerimeter(),myrp3.getArea())


pass
