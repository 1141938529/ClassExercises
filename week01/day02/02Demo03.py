allMoney = eval(input("请输入你的贷款总数"))
allYear = eval(input("请输入你的贷款年数"))
# print(allMoney+allYear)

monthMoney = (allMoney * 0.005) / (1 - (1 / (1 + 0.005) ** (allYear * 12)))
money = monthMoney * 12 * allYear

# print('月供是：',monthMoney)
# print('总还款数为',money)

print("月供是%.2f"%monthMoney)
print("总还款数为：%.2f"%money)
