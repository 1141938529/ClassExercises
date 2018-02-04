import re

mstr = '''
    setTimeout("ajax_post('book','ajax','id','1','sky','6bffd153bf8c3722e3c2e7cd23f74567','t','1515175044')","1000");
'''
mre = "*sky','(\w+)'?*"
re.match(mre,mstr)

