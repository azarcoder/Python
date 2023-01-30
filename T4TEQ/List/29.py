n=int(input())
a = [[int(j) for j in input().split()][:n] for i in range(n)]
b = [[int(j) for j in input().split()][:n] for i in range(n)]
e= [[0 for j in range(n)] for i in range(n)] #fill zero for all 


for i in range(n):
    for j in range(n):
        for k in range(n):
            e[i][j] += a[i][k] * b[k][j]

for i in e:
    print(*i)
