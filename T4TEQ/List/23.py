n=[int(i) for i in input().split()]
x=[];y=[]
for i in n:
    if i<=0:
        x.append(i)
    else:
        y.append(i)
x.sort()
y.sort()
y.extend(x)
print(y)
