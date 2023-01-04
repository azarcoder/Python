n=int(input())
for i in range(1,n+1):
    print((n-i)*' ',end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i,0,-1):
        if(i==1 or i==j):
            continue
        print(j,end="")
    print()