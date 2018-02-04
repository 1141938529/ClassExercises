# 习题2.4
pounds = eval(input("enter a value in pounds :"))
kilograms = pounds * 0.454
print(format(pounds), "pounds is ", kilograms, "kilograms.")

# 习题2.5

subtotal, graruityRate = eval(input("enter the subtotal and a graeuity rate :"))
gratuity = subtotal * graruityRate / 100
total = gratuity + subtotal
print("the gratuity is ", format(gratuity, ".2f"), "and the total is", format(total, ".2f"))

# 2.6

value = eval(input("enter a number between 0 and 1000:"))
ge = value % 10
bai = value // 100
shi = (value - ge - bai * 100) / 10
sum = int(ge + shi + bai)
print("the sum of the digits is ", sum)
