from tkinter import *


class mybtnWindow:
    def __init__(self):
        window = Tk()
        self.cbOkValue = IntVar()
        self.name = StringVar()
        # self.name.set("wowo")
        cbOk = Checkbutton(window, text="懵逼吗？",variable=self.cbOkValue,
                           bg = "red",
                           textvariable=self.name,command=self.CheckbuttonEvent)
        Radiobutton(window,text ="选我选我",justify="left").pack()
        cbOk["justify"] = "right"
        cbOk.pack()

        window.mainloop()

    def CheckbuttonEvent(self):
        print("OK",self.cbOkValue.get())
        # print(self.name.get()+"ss")

    pass
if __name__ == "__main__":
    mybtnWindow()
    pass