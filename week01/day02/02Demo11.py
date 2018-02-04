#   求当前时间
import time

allSeconds = int(time.time())
nowSeconds = allSeconds % 60
nowMins = (allSeconds // 60) % 60
nowHours = (allSeconds // 60 // 60) % 24
nowHours2 = (nowHours+8)%24
print("当前的时间为%.f时%.f分%.f秒" % (nowHours2, nowMins, nowSeconds))
