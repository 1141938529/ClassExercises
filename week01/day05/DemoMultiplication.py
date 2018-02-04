for i in range(1,10):
    for j in range(1,i+1):
        # print("%d*%d=%2d"%(j,i,i*j),end="  ")
        print(format("%d*%d=%2d"%(j,i,i*j),">8s"),end="")
        pass
    print("")