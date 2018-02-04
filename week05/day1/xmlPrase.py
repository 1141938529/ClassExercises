from xml.dom.minidom import parse
import xml.sax
from xml.sax import ContentHandler


class MyHandler(ContentHandler):
    def startElement(self, name, attrs):
        super(MyHandler, self).startElement(name, attrs)
        if name == "collection":
            self.movieList = []
        elif name == "movie":
            self.movieDict = {}
            self.movieDict["title"] = attrs["title"]

    def characters(self, content):
        super(MyHandler, self).characters(content)
        if len(content.strip()) > 0:
            self.content = content

    def endElement(self, name):
        super(MyHandler, self).endElement(name)
        if name == "collection":
            for item in self.movieList:
                print(item)
        elif name == "movie":
            self.movieList.append(self.movieDict)
        else:
            self.movieDict[name] = self.content

    pass


def domParseXml():
    # 获得当前文档
    dom = parse("./res/1.xml")
    # 获得 当前文档的标签tree ---->collection （Root（根）元素）
    domtree = dom.documentElement
    mstr = domtree.getAttribute("shelf")
    print(mstr)
    movies = domtree.getElementsByTagName("movie")
    mlist = []
    for movie in movies:
        mDict = {}

        # 属性值
        if movie.hasAttribute:
            title = movie.getAttribute("title")
            mDict["title"] = title

        mtype = movie.getElementsByTagName("type")[0].childNodes[0].data
        mDict["type"] = mtype
        format = movie.getElementsByTagName("format")[0].childNodes[0].data
        mDict["format"] = format
        if len(movie.getElementsByTagName("year")):
            year = movie.getElementsByTagName("year")[0].childNodes[0].data
            mDict["year"] = year
        if len(movie.getElementsByTagName("episodes")):
            episodes = movie.getElementsByTagName("episodes")[0].childNodes[0].data
            mDict["episodes"] = episodes
        rating = movie.getElementsByTagName("rating")[0].childNodes[0].data
        mDict["rating"] = rating
        stars = movie.getElementsByTagName("stars")[0].childNodes[0].data
        mDict["stars"] = stars
        description = movie.getElementsByTagName("description")[0].childNodes[0].data
        mDict["description"] = description

        mlist.append(mDict)
    for item in mlist:
        print(item)


if __name__ == '__main__':
    # domParseXml()
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(MyHandler())
    parser.parse("./res/1.xml")
    pass
