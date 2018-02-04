def reverse(number):
    Num =number
    myStr =""
    while number!=0:
        myStr += str(number%10)
        number = number//10
        # print(myStr)
        pass
    if int(myStr)== Num:
        return True
    else:
        return False
    pass
print(reverse(1234321))