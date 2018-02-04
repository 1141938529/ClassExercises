#  #0000ff = 蓝色
# #990000ff = 半透明蓝色
# 写一个函数，接收3-4个值得颜色通道
# 写一个showHexColor() 函数  返回改颜色的16进制字符串
# 调用showHexColor(100，255，00，00) 返回值为 "64ff0000"
# 调用showHexColor(255，00，00) 返回值为 "ff0000"
from myfile.BHDConverter import BHDConverter


def BHDConverterII(num):
    pass


def showHexColor(*args):
    res = ""
    for arg in args:
        # if (arg >= 0 and arg < 16):
        #     BHDC ="0"+ BHDConverter(arg)
        # else:
        #     BHDC = BHDConverter(arg)
        # # print(BHDC)
        # res += BHDC
        res += ("0" + BHDConverter(arg)) if (arg >= 0 and arg < 16) else BHDConverter(arg)
    return res


mystrs = input("请输入:")
if(len(mystrs.split(","))==3):
    redNo,greenNo,blueNo = eval(mystrs)
    print(showHexColor(redNo,greenNo,blueNo))
    pass
elif(len(mystrs.split(","))==4):
    arf,redNo, greenNo, blueNo = eval(mystrs)
    print(showHexColor( arf,redNo, greenNo, blueNo))
    pass

