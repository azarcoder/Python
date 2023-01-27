n=tuple([int(i) for i in input().split(',')])
s=''
for i in n:
    s+=str(i)
l=list(s)
e=[]
for i in l:
    if i not in e:
        e.append(i)
print(*e,sep=',')
