'''

n=tuple(input().split(','))
s=''
for i in n:
    s+=i[::-1]+','
print(s.strip(','))

'''
n=tuple([int(i[::-1]) for i in input().split(',')])
print(*n,sep=',')

