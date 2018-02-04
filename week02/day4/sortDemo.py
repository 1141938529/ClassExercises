from operator import itemgetter, attrgetter

from pip._vendor.html5lib.filters.sanitizer import attr_val_is_uri

from week02.day4.MyPerson import MyPerson

mlist = [("张三",21,"男"),("李四",24,"女"),
         ("王五",27,"女"),("老刘",25,"女"),("阿七",20,"男")]
mlist.sort(key=itemgetter(1))
print(mlist)
plist = [MyPerson("张三",21,"男"),MyPerson("李四",24,"女"),
         MyPerson("王五",27,"女"),MyPerson("老刘",25,"女"),MyPerson("阿七",20,"男")]
plist.sort(key=attrgetter("age"))
for item in plist:
    print(item)