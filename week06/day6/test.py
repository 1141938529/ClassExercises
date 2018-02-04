from collections import Counter

if __name__ == '__main__':
    c = Counter(["aa",12,12,21,78,"kill"])
    for k in c.keys():
        print(k)
    print(c.most_common())
    pass