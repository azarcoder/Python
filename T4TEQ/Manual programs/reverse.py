a=12322
r=0
while a:
    r=r*10+a%10
    a//=10
print(r)