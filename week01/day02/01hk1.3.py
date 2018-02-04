print('''
FFFFFFF   U     U   NN    NN
FF        U     U   NNN   NN
FFFFFFF   U     U   NN N  NN
FF         U   U    NN  N NN
FF          UUU     NN   NNN
''')

print("a", end=("      "))
print("a^2", end=("    "))
print("a^3")


def PRINt(a):
    print(format(str(a), "7s"), end=(""))
    print(format(str(a ** 2), "7s"), end=(""))
    print(format(str(a ** 3), "7s"), )


for i in range(4):
    PRINt(i + 1)



    # print(format("10","6s"),end="")
    # print("ssss")
