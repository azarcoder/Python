a=[int(i) for i in input().split(',')]
m=[];l=[]
for i in range(len(a)-2):
    for j in range(i+1,len(a)-1):
        for k in range(j+1,len(a)):
            if a[i]+a[j]+a[k]==0:
                m.append([a[i],a[j],a[k]])
print(m)

