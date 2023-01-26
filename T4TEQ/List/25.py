n=input().split()
c=0
for i in n:
    if len(i)>2 and i[0]==i[-1]:
            c+=1
print(c)
        
