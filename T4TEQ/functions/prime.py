n=int(input())
for i in range(2,n+1):
    f=True
    for j in range(2,i//2+1):
        if(i%j==0):
            f=False
            break
    if(f):
        print(i,end=' ')
