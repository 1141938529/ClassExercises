# 凤姐择偶
# 长得帅的而且有钱  你就从了凤姐吧
# 长得帅的但是没有钱  凤姐想和你做个朋友
# 长得不帅的而且没有钱  你就从了凤姐吧

isHandsome = input("你是否长得帅：Y/N")


isHandsome = True if isHandsome=="Y" else False

if(isHandsome):
    print("恭喜你进入第二轮面试:")
    isRich = input("你是否有钱：Y/N")
    isRich = True if isRich == "Y" else False
    if isRich:
        print("凤姐说要嫁给你")
    else:
        print("有多远滚多远呀")
        pass
else:
        print(" 哥屋恩   滚！")
        pass

