n=int(input())
p=1;s=0
while n:
    s+=n%10*p
    p*=2
    n//=10

