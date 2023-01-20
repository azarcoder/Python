ip = input()
s=''
c=''
m=0
for e in ip.lower():
    if e.isalpha():
        if e not in s:
            s+=e
            print(e,"-",ip.lower().count(e),end=' ')
        if ip.lower().count(e)>m:
            m=ip.lower().count(e)
            c=e
print('\n',c,sep='')
