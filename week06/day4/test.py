import re


class PwdException(RuntimeError):
    def __init__(self, pwd):
        super().__init__()
        self.pwd = pwd
        print("非法密码，长度应为6-12位")

    # def __str__(self):
    #     return "非法密码%s，长度应为6-12位"%(self.pwd)

    def handle(self):
        print("正在解决异常")

def register(name, passwd):
    try:
        if len(passwd) < 6 or len(passwd) > 12:
            raise PwdException(passwd)
    except PwdException as e:
        e.handle()

reTable = '<table .*?>([\s\S]+)</table>'
reTable = re.compile(reTable)

reDate = ".*?>([\w.\-%]+)<"
reDate = re.compile(reDate)
if __name__ == '__main__':
    # register("张三","123")
    # mstr = reTable.search('<table width="100%" id="table1">mmmmmmm   ,,</table>').group(1)
    # print(mstr)
    mstr1 = 'tr><td class="align_center "><a href="http://fund.stockstar.com/funds/000613.shtml">000613</a></td>'
    mstr2 = reDate.findall(mstr1)
    print(mstr2)
    pass