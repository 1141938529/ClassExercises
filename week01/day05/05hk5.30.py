import time
# print(time.time(),type(time.time())) 1506342825.779233 <class 'float'>
def getCurrentTime ():
    # /当前的描述
    currSecs = int(time.time())
    currYears = currSecs//(365*24*60*60) +1970
    CurrMonth = (currSecs-(currYears-1970)*365*24*3600)//(24*60*60*30)
    print(CurrMonth)
getCurrentTime()