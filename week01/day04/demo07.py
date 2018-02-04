# 猜数字游戏
# 规则：随机产生一个0-1000 的数字 用户进行输入数字
import random

answer = random.randint(1, 1000)
myAnswer = None

while myAnswer!=answer :
  myAnswer= eval( input("请猜一个数字（0-1000）:"))
  if myAnswer==-1 :
      print("老子不想玩了 gun")
      break
  else:
      if (myAnswer>1000 or myAnswer<0):
          print("骚年，睁大眼睛看看条件"
                "，请重新输入吧")
          continue
      else:
          if myAnswer>answer :
             print("太大了")
          elif myAnswer<answer:
              print("太小了")
              pass
          else:
              print("猜对了")
              pass

print("game over")
