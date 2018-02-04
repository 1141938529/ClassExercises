# /求出文件中所有的文件并且找出每个单词出现的频率
import os
import re
from collections import Counter


def getDocWordCounts(path):
    counter = Counter()
    if os.path.isdir(path):
        filelist = os.listdir(path)
        for filename in filelist:
            counter += getDocWordCounts(path + "/" + filename)
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


def getDocWordCounts2(path):
    # 如果为文件夹
    counter = Counter()
    if os.path.isdir(path):
        # 找到所有的文件（夹）
        filelits = os.listdir(path)
        # 遍历出所有的并递归出来
        for name in filelits:
            counter += getDocWordCounts2(path + "/" + name)
    # 如果为文本文档则进行处理
    elif os.path.isfile(path) and path.endswith(".txt"):
        # 读出文件内的内容text
        file = open(path, mode="r", encoding="utf-8")
        text = file.read()
        file.close()
        # 找出文本内的所有的单词
        wordlist = re.findall("[A-Za-z]+", text)
        # 统计出每个单词个数
        counter = Counter(wordlist)
    return counter
    pass


if __name__ == "__main__":
    # print(getDocWordCounts("./res").most_common())
    print(getDocWordCounts2("./res").most_common())
pass
