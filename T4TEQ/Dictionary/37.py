n=int(input())
m=[]
for i in range(n):
    x=[i for i in input().split()][:n+1]
    m.append(x)

d={}
for i in range(len(m)):
    n=m[i][0]
    ind=m[i][1:]
    s=sum([int(i) for i in ind])
    new_dict={n:s}
    d.update(new_dict)

'''
print(d)
3
Akil 90 95 96
abi 20 34 45
ravi 20 45 44
{'Akil': 281, 'abi': 99, 'ravi': 109}
'''
s= sorted(d.items(), key=lambda x:x[1],reverse=True)
for i in s:
    print(*i[0],sep='',end=' ')
        
        
    
