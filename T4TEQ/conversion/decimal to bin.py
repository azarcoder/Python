n=int(input())
s=0;j=1
while n:
    d=n%2
    s+=d*j 
    j*=10
    n//=2
print(s)