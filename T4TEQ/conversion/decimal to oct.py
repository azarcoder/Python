n=int(input());s=0;p=1
while n:
    d=n%8
    s+=d*p
    p*=10
    n//=8
print(s)
