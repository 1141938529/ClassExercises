import re
# <img class="skuImg" data-exposal="" data-src="http://img1.360buyimg.com/imgb/s280x280_jfs
# /t10858/283/122922559/204863/262a17c1/59c68f53N251c04d9.jpg" src="http://img1.360buyimg
# .com/imgb/s280x280_jfs/t10858/283/122922559/204863/262a17c1/59c68f53N251c04d9.jpg" data-done="1">
if __name__ == '__main__':
    # reImgUrl = '<img .*src="(.*?)".*>'
    # res = re.search(reImgUrl,'<img class="skuImg" data-exposal="" data-src="http://img1.360buyim'
    #                          'g.com/imgb/s280x280_jfs/t10858/283/122922559/204863/262a17c1/59c'
    #                          '68f53N251c04d9.jpg" src="http://img1.360buyimg.com'
    #                          '/imgb/s280x280_jfs/t10858/283/122922559/204863/262a17'
    #                          'c1/59c68f53N251c04d9.jpg" data-done="1">')
    # res2='http://img1.360buyimg.com/imgb/s280x280_jfs/t10858/283/' \
    # '122922559/204863/262a17c1/59c68f53N251c04d9.jpg'
    # reImgUrl2 = '.*/(.*\.jpg)'
    # res2 = re.search(reImgUrl2,res2)
    # print("******",res2.group(1))
    # print("******",res.group(1))

    reImgName = ".*\/(.*)"
    mstr = "http://p3.pstatp.com/large/433f000319a74df467ca"
    mstr = "http://p3.pstatp.com/large/433f000319b57ae5cb13"

    print(re.findall(reImgName,mstr))
    pass