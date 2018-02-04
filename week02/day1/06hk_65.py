def displaySortedNumbers(num1, num2, num3):
    numList = [num1, num2, num3]
    myMax = max(num1, num2, num3)
    myMin = min(num1, num2, num3)
    numList.remove(myMax)
    numList.remove(myMin)
    myMid = numList[0]
    print(myMin, myMid, myMax)
    pass



num1, num2, num3 = eval(input("请输入三个整数："))
print("这三个整数从小到大排序为：", end="")
displaySortedNumbers(num1, num2, num3)
