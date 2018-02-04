# 检测一个数字能否被5和6整除

value = eval(input("enter a integer:"))
Div5and6 = False
Div5Or6 = False
notDiv5And6 = False
if (value % 5 == 0):
    if (value % 6 == 0):
        Div5and6 = True
        pass
    else:
        Div5Or6 = True
        pass
    pass
else:
    if (value % 6 == 0):
        Div5Or6 = True
        pass
    else:
        notDiv5And6 = True
        pass

print("Is %d divisible 5 and 6? %s"%(value,str(Div5and6)))
print("Is %d divisible 5 or 6? %s"%(value,str(Div5Or6)))
print("Is %d divisible 5 or 6,but not both? %s"%(value,str(notDiv5And6)))
