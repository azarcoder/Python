n  = set([int(i) for i in input().split(',')])
n2 = set([int(i) for i in input().split(',')])
print('{}' if n&n2==set() else n&n2 ,n|n2)
#print(n&n2,n|n2)
