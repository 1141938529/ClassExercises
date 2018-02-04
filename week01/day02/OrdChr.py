# 使用ord函数找出1，A，B，a，b的ascII码
print("1的ASCII码为：",ord('1'))
print("A的ASCII码为：",ord('A'))
print("B的ASCII码为：",ord('B'))
print("a的ASCII码为：",ord('a'))
print("b的ASCII码为：",ord('b'))

# 使用chr函数找出40,59，79，85 90 所对应的字母
print("----------------")
c = 40
print("40的ASCII码为：",chr(40))
print(str(c)+"的ASCII码为：",chr(c))


def Ascll(c):
    print(str(c) + "的ASCII码为：", chr(c))

def main():
    Ascll(40)
    Ascll(59)
    Ascll(79)
    Ascll(85)
    Ascll(90)

main()

