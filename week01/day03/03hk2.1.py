# 习题2.1
import math

Celsius = eval(input("Enter a degree in Celsius:"))
# print(Celsius)
fahrenheit = (9/5)*Celsius +32
# print(fahrenheit)
print("%.f Celsius is %.1f Fahrenheit"%(Celsius,fahrenheit))

# 习题2.2

radius,length = eval(input("enter the radius and length of a cylinder:"))
raea  = radius *radius *math.pi
volume  =  raea *length
print("the area is %.4f"%raea)
print("the volume is %.1f"%volume)

# 习题2.3

feet = eval(input("enter a value for feet: "))
meters = feet*0.305
print("%.1f feet is %.4f meters."%(feet,meters))