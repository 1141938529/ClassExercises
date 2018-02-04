def reverse(number):
    Num = number
    myStr = ""
    while number != 0:
        myStr += str(number % 10)
        number = number // 10
        # print(myStr)
    print(int(myStr))
    pass

numPlz = eval(input("请输入一个整数："))
reverse(numPlz)
