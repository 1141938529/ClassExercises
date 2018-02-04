def getPentagonalNumber(n):
    num = n * (3*n - 1) / 2
    return num


for i in range(1,101):
    # num = getPentagonalNumber(i)
    print(format(int(getPentagonalNumber(i)),"5d"),end=" ")
    if ((i) % 10 == 0):
        print("")