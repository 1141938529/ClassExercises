
# 随机生成图片验证码
# 工具导入 graphic-verification-code
import os

import gvcode

img, code = gvcode.generate(font_file=r"C:\Windows\Fonts\微软雅黑\msyhbd.ttc")
# img.save("D:/mygraphic.png")
print(code)
img.show()
img.save("")
print(img)
