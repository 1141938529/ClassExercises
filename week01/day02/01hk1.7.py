def PI(n):
    b = 0
    for i in range(n):
        print(i)
        a = i % 2
        if (a == 0):
            b = b + 1 / (2 * i + 1)
            print(b)
        else:
            b = b - 1 / (2 * i + 1)
    print(b)
    return b * 4


print(PI(3))
