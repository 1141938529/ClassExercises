from matplotlib import pyplot

if __name__ == '__main__':
    mplot = pyplot.plot([1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8])
    for item in mplot:
        print(item)
    pyplot.show()
    pass
