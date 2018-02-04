import os
from tkinter import *
from tkinter import filedialog


class calulatonCodeNUms:
    def __init__(self):
        window = Tk()
        window.title("代码统计器")
        frame1 = Frame(window)
        frame1.pack()
        frame = Frame(window)
        frame.pack()

        self.totalLines = StringVar()
        self.blankLines = StringVar()
        self.commentLines = StringVar()
        self.effectiveLines = StringVar()
        self.dirpath = StringVar()

        self.totalLines.set("0 行")
        self.blankLines.set("0 行")
        self.commentLines.set("0 行")
        self.effectiveLines.set("0 行")

        Label(frame1, text="请选择要统计的文件（夹）").grid(row=1, column=1, padx=10, pady=3)
        Button(frame1, text="选择文件", command=self.getDirPath).grid(row=1, column=2, padx=10, pady=3)
        Label(frame, text="文件路径：").grid(row=1, column=1, padx=10, pady=3, sticky="E")
        Entry(frame, textvariable=self.dirpath, width=20).grid(row=1, column=2, padx=10, pady=3, sticky="W")
        Label(frame, text="总代码量：").grid(row=2, column=1, padx=10, pady=3, sticky="E")
        Label(frame, textvariable=self.totalLines).grid(row=2, column=2, padx=10, pady=3, sticky="W")
        Label(frame, text="总空行数：").grid(row=3, column=1, padx=10, pady=3, sticky="E")
        Label(frame, textvariable=self.blankLines).grid(row=3, column=2, padx=10, pady=3, sticky="W")
        Label(frame, text="总注释量：").grid(row=4, column=1, padx=10, pady=3, sticky="E")
        Label(frame, textvariable=self.commentLines).grid(row=4, column=2, padx=10, pady=3, sticky="W")
        Label(frame, text="有效代码：").grid(row=5, column=1, padx=10, pady=3, sticky="E")
        Label(frame, textvariable=self.effectiveLines).grid(row=5, column=2, padx=10, pady=3, sticky="W")

        Button(frame, text="开始统计", width=15, command=self.caluationLines).grid(row=6, column=1, columnspan=2,
                                                                               pady=(3, 10))
        window.mainloop()

    def getDirPath(self):
        # 选择打开文件的窗口
        path = filedialog.askdirectory()
        self.dirpath.set(path)
        pass

    def caluationLines(self):
        # 获取用户需要打开文件地址
        path = self.dirpath.get()
        # 如果为文件夹
        if os.path.isdir(path):
            pass
        # 如果为文件而且是py文件
        elif os.path.isfile(path) and path.endswith(".py"):

            pass
        # 如果为文件  但却不是py文件
        else:
            pass

        pass

    def calculationFileLines(self, path):
        # 分别初始化 空格行数 注释行数 有效行数
        totalLines = 0
        blankLines = 0
        commentLines = 0
        effectiveLines = 0
        # isComment 为false表示不再段注释中 true表示在段注释中
        isComment = False
        # 读取文件 lineslist存储每一行的数据的列表
        file = open(path, mode="r", encoding="utf-8")
        lineslist = file.readlines()
        file.close()
        totalLines = len(lineslist)
        # 统计每一行是否为空行、注释行、有效代码行
        for line in lineslist:
            # 判断是否为空行
            if line.strip() == "":
                blankLines += 1
            # 判断是否为段注释
            # 如果isComment==False 说明''' 是段注释的开头
            elif line.strip().startswith("'''") and line.strip().endswith("'''") and len(line.strip())>3:
                commentLines += 1
                print(line.strip())
            elif line.strip().startswith("'''") and isComment == False:
                commentLines += 1
                isComment = True
                print(line.strip())
            # 如果isComment==True 说明''' 是段注释结尾
            elif line.strip().endswith("'''") and isComment == True:
                commentLines += 1
                print(line.strip())
                isComment = False
            # 如果isComment==True 说明还在段注释中
            elif isComment == True:
                commentLines += 1
                print(line.strip())
            # 单行注释
            elif line.strip().startswith("#"):
                commentLines += 1
                print(line.strip())
            else:
                effectiveLines += 1
        if blankLines + commentLines + effectiveLines != totalLines:
            print("统计有误 结果都为零！")
            totalLines = 0
            blankLines = 0
            commentLines = 0
            effectiveLines = 0

        return blankLines, commentLines, effectiveLines,totalLines



if __name__ == "__main__":
    strs=calulatonCodeNUms().calculationFileLines("./test01.py")
    print(strs)