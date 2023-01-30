a=[int(i) for i in input().split(',')]
l=len(str(max(a)))
m=1
while l:
    n=[[],[],[],[],[],[],[],[],[],[]]
    for i in a:
        n[i%(m*10)//m].append(i)
    a=[]
    for i in n:
        if len(i)>0:
            for j in i:
                a.append(j)
    l-=1
    m*=10

print(*a)
