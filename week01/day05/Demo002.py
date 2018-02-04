Num = 0
a = 2
while True:
    count = 0
    for i in range(2, a ):
        if (a % i == 0):  # 能整除
            count += 1
        pass
    if (count == 0):
        Num += 1
        if (Num % 10 == 0):
            print(format(a, "4d"))
        else:
            print(format(a, "4d"), end="  ")
    if(Num == 50):
        break

    a += 1
