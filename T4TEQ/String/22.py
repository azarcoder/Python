n,f,r=input(),input(),input()
k=0
for i in n.split():
     k+=1
     if i==f:
          print(k%2 and r or i,end=" ")
     else:
          print(i,end=" ")
