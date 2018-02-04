import re

import requests

from week06.SpiderUtils import printList

url = 'http://www.baidu.com/s?wd=岛国%20邮箱'

'''
'''

reNet = 'href="(http.+?)"'
reNet = re.compile(reNet)

reEmail = "([a-z]|\d)([a-z]|\d|_)+@([a-z]|\d)+\.([a-z]|\d)+.*"
reEmail = re.compile(reEmail)

index = 0
def getEmailNet(url):
    global index
    index +=1
    html = requests.get(url).text
    # emailList = reEmail.findall(html)
    netList = reNet.findall(html)
    if index<=2:
        print(index)
        for net in netList:
            netList+=getEmailNet(net)
        print(index)
    return netList


mdict = {}

if __name__ == '__main__':
    netList = getEmailNet(url)
    printList(netList)



    pass
