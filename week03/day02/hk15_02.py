# 递归实现费尔巴切
def fib(n):
    if (n > 2):
        mysum = fib(n - 1) + fib(n - 2)
    elif n == 2:
        mysum = 1
    elif n == 1:
        mysum = 0
    return mysum


# 迭代实现费尔巴切
def fib1(n):
    mysum = 0
    count1 = 0
    count2 = 0
    for i in range(1, n):
        if i == 1:
            mysum = 0
            count2 = 0
        elif i == 2:
            mysum = 1
            count2 = 1
        elif i > 2:
            count1 = mysum
            mysum = count2
            pass
        count2 = mysum + count1
    return count2


if __name__ == "__main__":
    print(fib(12))
    print(fib1(12))
