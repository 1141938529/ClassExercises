from week02.homework.geometricobject import GeometricObject


class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        pass

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def setSide1(self, side1):
        self.__side1 = side1

    def setSide2(self, side2):
        self.__side2 = side2

    def setSide3(self, side3):
        self.__side3 = side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3)/2
        return (s*(s-self.__side1)*(s-self.__side2)*(s-self.__side3))**(1/2)

    def getPerimeter(self):
        return (self.__side1 + self.__side2 + self.__side3)
    def __str__(self):
        return ("Triangle:side1=%.2f side2=%.2f side3=%.2f"%(self.__side1,self.__side2,self.__side3))

    pass

if __name__ == "__main__" :
    s1,s2,s3 = eval(input("请输入三角形的三边长："))
    color = input("颜色：")
    isFilled = eval(input("是否填充（1代表填充 0代表不填充）："))
    myTri = Triangle(s1,s2,s3)
    myTri.setColor(color)
    myfil = True if isFilled==1 else False
    myTri.setFilled(myfil)
    print("这个三角形的面积为：%.2f，周长为：%.2f，颜色为：%s，是否填充颜色：%s"
          %(myTri.getArea(),myTri.getPerimeter(),myTri.getColor(),str(myTri.isFilled())))
    pass