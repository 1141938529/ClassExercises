import random
from tkinter import *
from tkinter import messagebox


class verCodeGenerator:
    def __init__(self):
        window = Tk()
        window.title("验证码生成器")
        frame1 = Frame(window)
        frame2 = Frame(window)
        frame1.pack()
        frame2.pack()
        self.grounps = StringVar()
        self.counts = StringVar()
        self.Vercode = StringVar()
        Label(frame1, text="生成组数：", width=10).grid(row=1, column=1)
        Entry(frame1, width=10, textvariable=self.grounps).grid(row=1, column=2)
        Label(frame2, text="每组个数：", width=10).grid(row=1, column=1)
        Entry(frame2, width=10, textvariable=self.counts).grid(row=1, column=2)
        Button(window, text="生成验证码", command=self.CodeGenerator).pack(side=RIGHT)
        Label(window, bg="white", width=30, textvariable=self.Vercode).pack(side=BOTTOM)
        window.mainloop()
        pass

    def CodeGenerator(self):
        if (self.counts.get().isdigit()) and (self.grounps.get().isdigit()):
            poplution = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            totalList = []
            for i in range(int(self.grounps.get())):
                mlist = random.sample(poplution, int(self.counts.get()))
                mstr1 = "".join(mlist)
                totalList.append(mstr1)
            mstr2 = "-".join(totalList)
            self.Vercode.set(mstr2)
        else:
            messagebox.showerror("错误", "请输入数字！")

    pass


if __name__ == "__main__":
    verCodeGenerator()
