import math

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
count = 0
for i in range(2,10000):
    if(isPrimeII(i)):
        count += 1
print("10000以内的素数的总数为%d"%count)
