import csv
import json
import xml.sax
from xml.sax import ContentHandler
from xml.dom.minidom import parse
from myfile.OfficeUtil import *

class Cat():
    def __init__(self,nickname,haircolor,like_foods):
        self.nickname = nickname
        self.haircolor = haircolor
        self.like_foods = like_foods

class MyHandler(ContentHandler):
    def startElement(self, name, attrs):
        super(MyHandler, self).startElement(name, attrs)
        if name == "Catlist":
            self.catsList = []
        elif name == "cat":
            self.catDict = {}


    def characters(self, content):
        super(MyHandler, self).characters(content)
        if len(content.strip())>0:
            self.content =content

    def endElement(self, name):
        super(MyHandler, self).endElement(name)
        if name == "Catlist":
            print(self.catsList)
        elif name == "cat":
            self.catsList.append(self.catDict)
        else:
            self.catDict[name] = self.content
    pass

'''
{"name": "嘟嘟", "haircolor": "花色", "like_foods": ["可乐", "啤酒"]},
{"name": "摩卡", "haircolor": "纯白色", "like_foods": ["狗粮", "面包", "小花生"]},
{"name": "苏拉", "haircolor": "灰色", "like_foods": ["junkfood", "辣条"]},
{"name": "思诺", "haircolor": "暗黑色", "like_foods": ["米饭", "面条"]},
{"name": "小煤球", "haircolor": "碎花色", "like_foods": ["鱼", "老鼠"]}
'''


def jsonParse():
    file = open("./res/猫咪.json", mode="r", encoding="utf-8")
    mstr = file.read()
    file.close()
    jsonstr = json.loads(mstr)
    print(jsonstr)


def saxParseXml():
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(MyHandler())
    parser.parse("./res/猫咪.xml")


def domParseXml():
    rootNode = parse("./res/猫咪.xml")
    rootElement = rootNode.documentElement
    cats = rootElement.getElementsByTagName("cat")
    catlist = []
    for cat in cats:
        catDicts = {}
        nickname = cat.getElementsByTagName("nickname")[0].childNodes[0].data
        catDicts["nickname"] = nickname
        haircolor = cat.getElementsByTagName("haircolor")[0].childNodes[0].data
        catDicts["haircolor"] = haircolor
        like_foods = cat.getElementsByTagName("like_foods")[0].childNodes[0].data
        catDicts["like_foods"] = like_foods
        catlist.append(catDicts)
    print(catlist)


def writeCsv2():
    fileobject = open("./res/猫咪.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(fileobject)
    writer.writerow(["昵称", "毛色", "喜欢的食物"])
    for cat in catList:
        writer.writerow([cat.nickname, cat.haircolor, cat.like_foods])
    fileobject.close()
    csv.writer(fileobject)


if __name__ == '__main__':

    doudou = Cat("嘟嘟","花色",["可乐", "啤酒"])
    moka = Cat("摩卡","纯白色",["狗粮", "面包", "小花生"])
    sula = Cat("苏拉","灰色",["junkfood", "辣条"])
    sinuo = Cat("思诺","暗黑色",["米饭", "面条"])
    meiqiu = Cat("小煤球","碎花色",["鱼", "老鼠"])
    catList = [doudou,moka,sula,sinuo,meiqiu]
    catList2 = []
    for cat in catList:
        mdicts = {}
        mdicts["昵称"] = cat.nickname
        mdicts["毛色"] = cat.haircolor
        mstr = ""
        for item in cat.like_foods:
            mstr =mstr+ " "+item
        mdicts["喜欢的食物"] = mstr
        catList2.append(mdicts)
    # print(catList2)
    jsonParse()
    # saxParseXml()
    # domParseXml()
    # writeCsv()
    # writeCsv(catList2,"./res/猫咪2.csv")
    print("main over")