# 求出一个文件内的文本文档中的单词频数
import os
import re
from collections import Counter


def docWordFrequency(path):

    counter = Counter()
    if os.path.isdir(path):
        mdirlist = os.listdir(path)
        for fname in mdirlist:
            counter += docWordFrequency(path+"/"+fname)
        pass
    elif os.path.isfile(path) and path.endswith(".txt"):
        file = open(path, mode="r", encoding="utf-8")
        text = file.read()
        file.close()
        mlist = re.findall("[A-Za-z]+", text)
        counter = Counter(mlist)
    else:
        pass
    return counter
    pass


if __name__ == "__main__":
    counter = docWordFrequency("../")
    print(counter.most_common())
    pass
