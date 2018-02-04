#    习题4.9 比较2中包装的大米的优惠

weight1, price1 = eval(input("enter weight and price for package1"
                             ":"))
weight2, price2 = eval(input("enter weight and price for package1"
                             ":"))
if((price1/weight1)<(price2/weight2)):
    print("package 1 has the better price")
    pass
elif((price1/weight1)==(price2/weight2)) :
    print("package 1 and 2 both of  OK")
    pass
else:
    print("package  2 has the better price")
    pass