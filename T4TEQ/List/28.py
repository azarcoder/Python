x=int(input())
m=[[j for j in input().split()]for i in range(x)]
l=0;u=0
for i in range(x):
    for j in range(x):
        if i>j:
            l+=int(m[i][j])
        if i<j:
            u+=int(m[i][j])
print(u-l)
