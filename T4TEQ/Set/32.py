n=set([int(i) for i in input().split(',')])
n2=set([int(i) for i in input().split(',')])
print(n.symmetric_difference(n2))

print(n^n2)
