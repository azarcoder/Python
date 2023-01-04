n=int(input())
for i in range(1,n+1):
    print((n-i)*' ',end='') 
    c=1 
    for j in range(1,i+1):
        print(c,' ',sep='',end='')
        c=c*(i-j)//j
    print()