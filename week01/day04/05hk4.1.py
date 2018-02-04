import math

a, b, c = eval(input("enter a,b,c:"))
deDa = b ** 2 - 4 * a * c
if (deDa > 0):
    r1 = (-b + math.sqrt(deDa)) / (2 * a)
    r2 = (-b - math.sqrt(deDa)) / (2 * a)
    print("the roots are %f and %f" % (r1, r2))
    pass
elif (deDa==0):
    r = (-b) / (2 * a)
    print("the root is  ",r)
    pass
else:
    print("the equation has no real roots")
    pass
