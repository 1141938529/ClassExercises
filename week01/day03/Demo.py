import math

print(math.sqrt(3.2333332))

money = eval(input("enter the moneyly saveing amount:"))
def totalMoney(baseMoney,months):
    money = 0
    for i in range(months):
        money = (baseMoney+money)*(1+0.00417)
    return money

print("after the sixeth month,the account value is ",
      format(totalMoney(money,6),".2f"))
