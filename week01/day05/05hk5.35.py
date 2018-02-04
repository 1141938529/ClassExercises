def findAllFactor(num):
    allFactorList = []
    for i in range(1,num+1):
        if (num%i==0):
            if(num != i):
                allFactorList.append(i)
    # print(allFactorList)
    return allFactorList

for i in range(1,10000):
    if(i == sum(findAllFactor(i))):
        print(i,end="  ")