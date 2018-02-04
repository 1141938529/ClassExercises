import pickle
from tkinter import *

from week03.day03.personMessage import personMessage

PATH = "./contacts.dat"
permsgList = []


class contactsInterface:
    def __init__(self):
        self.curIndex = 0
        # 初始化
        # 读取整个文件中的数据 形成一个列表
        # 打开文件  逐个读取permsg对象信息并存入permsgList中
        try:
            file = open(PATH, mode="rb")
            while True:
                try:
                    permsg = pickle.load(file)
                    # print(permsg)
                    permsgList.append(permsg)
                # 如果出现【EOFError】异常,这说明内容读完了
                except EOFError:
                    break
            file.close()
        except:
            pass

        # 界面布局结构
        window = Tk()
        window.title("联系人管理器")
        frame1 = Frame(window)
        frame1.pack()

        self.namemsg = StringVar()
        self.telmsg = StringVar()
        self.qqmsg = StringVar()
        self.emailmsg = StringVar()
        self.adrressmsg = StringVar()

        # 给每个entry设置初始值
        if len(permsgList) > 0:
            self.setPersonMsg(0)

        # 姓名布局
        frame2 = Frame(frame1)
        Label(frame2, text="姓名:", width=5).grid(row=1, column=1, padx=10, pady=10)
        Entry(frame2, width=20, textvariable=self.namemsg).grid(row=1, column=2)
        frame2.grid(row=1, column=1)

        # 电话布局
        frame3 = Frame(frame1)
        Label(frame3, text="电话:", width=5).grid(row=1, column=1, padx=10, pady=10)
        Entry(frame3, textvariable=self.telmsg).grid(row=1, column=2)
        frame3.grid(row=1, column=2)

        # QQ布局
        frame4 = Frame(frame1)
        Label(frame4, text="QQ:", width=5).grid(row=1, column=1, padx=10, pady=10)
        Entry(frame4, textvariable=self.qqmsg).grid(row=1, column=2)
        frame4.grid(row=2, column=1)

        # email布局
        frame5 = Frame(frame1)
        Label(frame5, text="email:", width=5).grid(row=1, column=1, padx=10, pady=10)
        Entry(frame5, textvariable=self.emailmsg).grid(row=1, column=2)
        frame5.grid(row=2, column=2)

        # 地址布局
        frame6 = Frame(frame1)
        Label(frame6, text="地址:", width=5).grid(row=1, column=1, padx=10, pady=10)
        Entry(frame6, width=50, textvariable=self.adrressmsg).grid(row=1, column=2)
        frame6.grid(row=3, column=1, columnspan=2)

        # 整个button的布局
        frame7 = Frame(frame1)
        Button(frame7, text="<<", width=5, command=self.btnFirst).grid(row=1, column=1, padx=(0, 5))
        Button(frame7, text="Prev", width=5, command=self.btnPrev).grid(row=1, column=2, padx=(0, 5))
        Button(frame7, text="Next", width=5, command=self.btnNext).grid(row=1, column=3, padx=(0, 5))
        Button(frame7, text=">>", width=5, command=self.btnLast).grid(row=1, column=4, padx=(0, 5))
        Button(frame7, text="Add", width=5, command=self.btnAdd).grid(row=1, column=5, padx=(0, 5))
        Button(frame7, text="Del", width=5, command=self.btnDel).grid(row=1, column=6, padx=(0, 5))
        frame7.grid(row=4, column=1, columnspan=2)

        window.mainloop()

    def btnFirst(self):
        self.curIndex = 0
        self.setPersonMsg(0)
        pass

    def btnPrev(self):
        # 先判断是否为第一个，如果是就不改变
        if self.curIndex > 0:
            self.setPersonMsg(self.curIndex - 1)
            self.curIndex -= 1
        pass

    def btnNext(self):
        # 先判断是否为最后一个，如果是就不改变
        if self.curIndex + 1 < len(permsgList):
            self.setPersonMsg(self.curIndex + 1)
            self.curIndex += 1
        pass

    def btnLast(self):
        self.curIndex = len(permsgList) - 1
        self.setPersonMsg(len(permsgList) - 1)
        pass
    # 增加事件
    def btnAdd(self):
        # 将新建的表格中的数据读取出来
        personmsg = personMessage(self.namemsg.get(), self.telmsg.get(),
                                  self.qqmsg.get(), self.emailmsg.get(), self.adrressmsg.get())
        file = open(PATH, mode="ab")
        pickle.dump(personmsg, file)
        file.close()
        # 创建对象
        permsgList.append(personmsg)
        # 新增信息后将当前的index设为最新的  并且显示
        self.curIndex = len(permsgList) - 1
        self.setPersonMsg(self.curIndex)
        pass

    # 删除事件
    def btnDel(self):
        # 如果permsgList内容为空时
        if len(permsgList) == 0:
            self.namemsg.set("")
            self.telmsg.set("")
            self.qqmsg.set("")
            self.emailmsg.set("")
            self.adrressmsg.set("")
            pass
        # 如果permsgList只剩下一个时 ，再删除显示的时候就需要清空所有
        # 并且将文件的内容也清空
        elif len(permsgList) == 1:
            permsgList.pop(self.curIndex)
            self.namemsg.set("")
            self.telmsg.set("")
            self.qqmsg.set("")
            self.emailmsg.set("")
            self.adrressmsg.set("")
            file = open(PATH, mode="wb")
            file.close()
        # 删除当前元素 并且把文件重新覆写一遍
        else:
            permsgList.pop(self.curIndex)
            if self.curIndex > len(permsgList) - 1:
                self.curIndex = len(permsgList) - 1
            self.setPersonMsg(self.curIndex)

            file = open(PATH, mode="wb")
            for permsg in permsgList:
                pickle.dump(permsg, file)
            file.close()

    pass

    # 给每个entery设置值
    def setPersonMsg(self, n):
        self.namemsg.set(permsgList[n].name)
        self.telmsg.set(permsgList[n].tel)
        self.qqmsg.set(permsgList[n].qq)
        self.emailmsg.set(permsgList[n].email)
        self.adrressmsg.set(permsgList[n].adress)


if __name__ == "__main__":
    contactsInterface()
