# 解析文件2中方法
import xml
from xml.dom.minidom import parse
from xml.sax import ContentHandler


class MyHandler(ContentHandler):
    def startElement(self, name, attrs):
        super(MyHandler, self).startElement(name,attrs)
        if name == "collection":
            self.mlist = []
        elif name == "movie":
            self.mdicts = {}


    def characters(self, content):
        super(MyHandler, self).characters(content)
        if  len(content.strip())>0:
            self.content =content
    def endElement(self, name):
        super(MyHandler, self).endElement(name)
        if name == "collection":
            # self.mlist.append(self.mdicts)
            print(self.mlist)
        elif name == "movie":
            self.mlist.append(self.mdicts)
        else:
            self.mdicts[name] = self.content
    pass


def domParseXml():
    dom = parse("./res/1.xml")
    domstree = dom.documentElement
    movies = dom.getElementsByTagName("movie")
    # movies2 = domstree.getElementByTagName("movie")
    # print(movies1)
    # print(movies2)
    mlist = []
    for item in movies:
        mdicts = {}
        if item.hasAttribute:
            title = item.getAttribute("title")
            mdicts["title"] = title
        mtype = item.getElementsByTagName("type")[0].childNodes[0].data
        mdicts["type"] = mtype
        format = item.getElementsByTagName("format")[0].childNodes[0].data
        mdicts["format"] = format
        if len(item.getElementsByTagName("year")):
            year = item.getElementsByTagName("year")[0].childNodes[0].data
            mdicts["year"] = year
        rating = item.getElementsByTagName("rating")[0].childNodes[0].data
        mdicts["rating"] = rating
        stars = item.getElementsByTagName("stars")[0].childNodes[0].data
        mdicts["stars"] = stars
        description = item.getElementsByTagName("description")[0].childNodes[0].data
        mdicts["description"] = description
        if len(item.getElementsByTagName("episodes"))>0:
            episodes = item.getElementsByTagName("episodes")[0].childNodes[0].data
            mdicts["episodes"] = episodes
        mlist.append(mdicts)
    return mlist


def saxParseXml():
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(MyHandler())
    parser.parse("./res/1.xml")


if __name__ == '__main__':
    # print(domParseXml())
    saxParseXml()

    pass