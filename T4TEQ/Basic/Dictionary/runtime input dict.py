n=int(input())
x=[i for i in input().split()][:n]
y=[i for i in input().split()][:n]
d=zip(x,y)
#d={key:value for (key,value) in zip(x,y)}
print(dict(d))
