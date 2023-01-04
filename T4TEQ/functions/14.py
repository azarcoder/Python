n=int(input())
def pm(n):
    f=True
    for i in range(2,n+1):
        if(n%i==0):
            f=False
            break
        if(f):
            return n 

for i in range(2,n//2+1):
    for j in range(2,n//2+1):
        if pm(i)+pm(j)==n:
            break
             

