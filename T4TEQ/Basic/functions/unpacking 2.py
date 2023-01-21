#unpacking 2
def demo(*n):
    print(n[0])
    n=list(n)
    n[0]='azar'
    n[1]='u'
    n[2]='deen'
    print(n)

demo('azar','t4teq','trichy','city')

#accessing dictionary items
def dd(**k):
    for i in k.keys():
        print("%s=>%s"%(i,k[i]))

dd(name="azar",age="21")

