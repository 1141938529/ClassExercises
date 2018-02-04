# date  = eval(python demo003.py < input.txt)
# print(format("","10"),end="")
# print("ssss")

for i in range(5):
    for j in range(i):
        if j == 0:
            print(format("",str((5 - i) * 4)), end="")
        print(format(j, "4d"), end="")
    print("")
