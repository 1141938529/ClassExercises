import gvcode


chars = "我的什么哈习思卡1234565745879"
img,code =gvcode.generate(size=(240,60),chars=chars,bg_color=(255,0,0),fg_color=(0,255,0),length=6)
img.show()
print(code)