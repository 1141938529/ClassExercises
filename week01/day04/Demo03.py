# 凤姐择偶
# 长得帅的而且有钱  你就从了凤姐吧
# 长得帅的但是没有钱  凤姐想和你做个朋友
# 长得不帅的而且没有钱  你就从了凤姐吧

isHandsome = input("请问你是否长得帅Y/N：")
isRich = input("请问你是否有钱Y/N：")

isHandsome = True if isHandsome=="Y" else False
isRich = True if isRich=="Y" else False

if isHandsome and isRich:
    print("你就从了凤姐吧")
    pass
elif isHandsome or isRich:
    print("凤姐想和你做个朋友")
    pass
else:
    print("有多远滚多远")
    pass
