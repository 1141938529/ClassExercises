def primeNumber():
    primeNumber = []
    for i in range(2, 100):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            primeNumber.append(i)
    return primeNumber

print(primeNumber())