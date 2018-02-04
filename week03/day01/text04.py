from tkinter import *


class MyTestwidget:
    def __init__(self):
        window = Tk()
        frame = Frame(window)
        frame.pack()
        self.isOk = IntVar()
        Checkbutton(frame,text="是否同意",bg="gray",variable=self.isOk,command = self.cbtnEvent).grid(row=1,column=1)
        Radiobutton(frame,text="红色",bg="red",value =1,variable = self.rbvalue,command=self.rbtnEvent).grid(row=1,column=2)
        Radiobutton(frame,text="绿色",bg="green",value =2,variable = self.rbvalue,command=self.rbtnEvent).grid(row=1,column=3)
        Radiobutton(frame,text="蓝色",bg="blue",value =3,variable = self.rbvalue,command=self.rbtnEvent).grid(row=1,column=4)
        window.mainloop()

    def cbtnEvent(self):
        print("同意" if self.isOk.get() else "不同意")
if __name__ == "__main__":
    MyTestwidget()