#kwargs
'''
values() - value only
keys() - key only
items() - both key,value
'''

#values
'''
def demo(**k):
    s=''
    for w in k.values():
        s+=w+' '
    return s

print("sentence:",demo(a="azarudeen",b="is",c="filmmaker"))
'''
#keys
'''
def demo(**k):
    s=''
    for w in k.keys():
        s+=w+' '
    return s

print("sentence:",demo(a="azarudeen",b="is",c="filmmaker"))
'''
#items
def demo(**k):
    r=[]
    for i,j in k.items():
        r.append("{} => {}".format(i,j))
    return r

print("sentence:",demo(a="azarudeen",b="is",c="filmmaker"))
