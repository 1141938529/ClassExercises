import re

if __name__ == '__main__':
    pattern = "1[35789][0-9]{9}"
    mstr1= "18070493584,12354687958,15942659876"
    mstr2= "ssssssssss18070493584,12354687958,15942659876"
    mstr3= "aasa18070493584,sa12354687958,sas15942659876"
    res1 = re.match(pattern,mstr1)
    res2 = re.search(pattern,mstr1)
    res3 = re.search(pattern,mstr1)
    res4 = re.search(pattern,mstr2)
    res5 = re.findall(pattern,mstr3)
    print(res1)
    print(res2)
    print(res3)
    print(res4)
    print(res5)
    pass
