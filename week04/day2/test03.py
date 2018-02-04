import threading

data = 0

addLock = threading.Lock()
# 处理进程冲突的第一种方式  if addLock.acquire():/addLock.release()
def aDD():
    global data
    if addLock.acquire():
        for i in range(1000000):
            data += 1
        addLock.release()
        print(threading.current_thread().getName()+"   Data=",data)
# 处理进程冲突的第二种方式  with addlock
def aDD2():
    global data
    with addLock:
        for i in range(1000000):
            data += 1
        # addLock.release()
        print(threading.current_thread().getName()+"   Data=",data)

if  __name__ =="__main__":
    for i in range(5):
        threading.Thread(target=aDD2,name="theard"+str(i)).start()
    pass
