n=int(input())
d={}
for i in range(n):
    #s,s2=[i for i in input().split()]
    #x={s:s2}
    #d.update(x)
    a=input().split()
    d[a[0]]=a[1]
print(d)

