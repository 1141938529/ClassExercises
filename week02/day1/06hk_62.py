def sumDigits(n):
    Mysum = 0
    while n != 0:
        Mysum += n % 10
        n = n // 10
    return Mysum
    pass
print(sumDigits(56325))