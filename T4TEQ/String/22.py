n,f,r=input(),input(),input()
k=0
for i in n.split():
    if i==f:
        k+=1
        print(k%2 and r or i,end=' ')
    else:
        print(i,end=' ')                  
