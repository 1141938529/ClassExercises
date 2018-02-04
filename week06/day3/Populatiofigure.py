from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['SimHei']
#  用来正常显示中文标签
pyplot.rcParams['axes.unicode_minus'] = False

p1 = pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], "r:")

p2 = pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], "b-.")
pyplot.title("两条直线图")
pyplot.xlabel("X轴",verticalalignment="top")
pyplot.ylabel("Y轴",override = {'fontsize': 'small','verticalalignment': 'center','horizontalalignment':'right','rotation':'vertical'})
pyplot.savefig("./figure1.png")

pyplot.show()
