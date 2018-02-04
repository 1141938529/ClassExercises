import math


def isPrime(num):
    prime = True
    if (num < 2):
        prime = False
    for i in range(2, int(num / 2) + 1):
        if (num % i == 0):
            prime = False
            break
    return prime
    pass


def isPrimeII(num):
    prime = True
    if (num < 2):
        prime = False
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            prime = False
            break
    return prime
    pass


for i in range(200):
    if (isPrime(i)):
        print(i, end=" ")
        pass
print("")
for i in range(200):
    if (isPrimeII(i)):
        print(i, end=" ")
        pass
