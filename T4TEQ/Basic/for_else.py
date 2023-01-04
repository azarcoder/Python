"""
n=5
for i in range(n,0,-1):
    print(i,end=" ")
print()
x='Hello world!'
c=0
for i in x:
    print(f'x[{c}]={i}')
    c+=1
list_of_fruits=['apple','banana','orange','kiwi','mango','tomoato','dates','papaya']
for x in list_of_fruits:
    print(f'i like {x}',end=' ')
"""
#for else
for i in range(1,6):
    if i==3:
        break
    print(i,end=" ")
else:
    print("end:)")

"""
else will work
1. when for complete it's iteration
2.if for iteration will be wrong

else won't work
1.when for break in specific condition
"""
print()
i=1
while i<=3:
    print(i,end=" ")
    if(i==2):
        break
    i+=1
else:
    print("wow else running")