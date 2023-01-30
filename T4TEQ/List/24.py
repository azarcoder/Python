l=[0,1]
while True:
    n=int(input())
    while(l[-1]<=n):
        l.append(l[-2]+l[-1])

    for i in l:
        if i<=n:
            print(i,end=' ')
        else:
            break
    s=input("do you want continue:(Y/N)")
    if(s=='N' or s== 'n'):
        break
