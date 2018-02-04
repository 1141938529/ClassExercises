from tkinter import *


class myWidgets:
    def __init__(self):
        window = Tk()
        farme1 = Frame(window)
        farme2 = Frame(window)
        farme1.pack()
        farme2.pack()
        self.cbvalue = IntVar()
        self.rbvalue = IntVar()
        Checkbutton(farme1, text="cButton", variable=self.cbvalue, command=self.cButtonEvent).grid(row=1,column=1)
        Radiobutton(farme1, text="红色", bg="red", value=1, variable=self.rbvalue, command=self.rButtonEvent).grid(row=1,column=2)
        Radiobutton(farme1, text="绿色", bg="green", value=2, variable=self.rbvalue, command=self.rButtonEvent).grid(row=1,column=3)
        Radiobutton(farme1, text="蓝色", bg="blue", value=3, variable=self.rbvalue, command=self.rButtonEvent).grid(row=1,column=4)
        window.mainloop()
    def cButtonEvent(self):
        pass
    def rButtonEvent(self):
        pass
    pass
if __name__ =="__main__" :
    myWidgets()