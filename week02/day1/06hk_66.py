def displayPattern(n):
    for i in range(n):
        if(i==n-1):
            print("",end="")
        else:
             print(format("",str(2*(n-i-1))),end="")
        for j in range(i+1,0,-1):
            print(format(j,"2d"),end="")
            pass
        print("")
    pass
displayPattern(5)