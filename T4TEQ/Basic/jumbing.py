n=int(input());s=0
while n:
    if n%10==3:
        continue
    s+=n%10
    n//=10
print(s)