def test(*args,**kwargs):
    return args,kwargs

print(test("a","b","c",key="aa",key2="bb"))