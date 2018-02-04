import os
from collections import Counter
from tkinter import *
from tkinter import messagebox


class getDocWordCounts:
    def __init__(self):
        window = Tk()
        frame1 = Frame(window)
        frame1.pack()
        frame2 = Frame(window)
        frame2.pack()
        self.mypath = StringVar()
        self.mytext= StringVar()
        Label(frame1,text="请输入文件(夹)路径：").grid(row=1,column=1)
        Entry(frame1,width=30,textvariable = self.mypath).grid(row=1,column=2)
        Button(frame2,text="开始统计",command=self.btnEvent).grid(row=1, column=3)
        Message(window,bg="gray",textvariable=self.mytext).pack(side=BOTTOM)
        # Entry(frame1, width=30, textvariable=path)
        window.mainloop()
        pass
    def btnEvent(self):   
        if os.path.exists(self.mypath.get()):
            path = self.mypath.get()
            counter = self.getCounter(path)
            # counter = self.getDocWordCounts(path)
            self.mytext.set(counter.most_common())
        else:
            messagebox.showerror("错误","请输入正确的文件（夹）地址！")
        pass

    def getCounter(self,path):
        counter = Counter()
        if os.path.isdir(path):
            flieList = os.listdir(path)
            for fliename in flieList:
                counter += self.getCounter(path + "/" + fliename)
        elif os.path.isfile(path) and path.endswith(".txt"):
            file = open(path, mode="r", encoding="utf-8")
            text = file.read()
            file.close()
            mlist = re.findall("[A-Za-z]+", text)
            print(path)
            counter = Counter(mlist)
        else:
            pass
        return counter
    def getDocWordCounts(self,path):
        counter = Counter()
        if os.path.isdir(path):
            filelist = os.listdir(path)
            for filename in filelist:
                counter += self.getDocWordCounts(path + "/" + filename)
        elif os.path.isfile(path) and path.endswith(".txt"):
            file = open(path, mode="r", encoding="utf-8")
            text = file.read()
            file.close()
            mlist = re.findall("[A-Za-z]+", text)
            counter = Counter(mlist)
            pass
        else:
            pass
        return counter

if __name__ =="__main__":
    getDocWordCounts()
    pass