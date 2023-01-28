x=int(input())
m=[]
for i in range(x):
    m.append([int(i) for i in input().split()][:x])
print(m)
