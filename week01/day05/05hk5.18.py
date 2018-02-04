# 求一个数以内的质数集合
def Primenumber(num):
    myPrimeList = []
    for i in range(2, num+1):
        # 判断一个数是否为质数
        count = 0
        for j in range(1, i+1):
            if (i % j == 0):
                count += 1
                if count > 2:
                    break
            if (j == i):
                myPrimeList.append(i)
    # print(myPrimeList)
    return myPrimeList
pass
# 求一个数的所有最小质因子
def allMinFactor (num3):
    # myList 用来装所有的质因子
    myList = []
    myPrimeList = Primenumber(num3)
    print(myPrimeList)
    for i in range(len(myPrimeList)):
        while True:
            num3 = num3 /  myPrimeList[i]
            myList.append(myPrimeList[i])
            if not (num3 % myPrimeList[i]==0):
                break
                pass
        if(num3 == 1):
            break
        pass
    return myList
print(allMinFactor(120))