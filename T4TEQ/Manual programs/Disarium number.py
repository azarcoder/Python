a=int(input());t=t2=a
x=0;r=0
while a:
    a//=10
    x+=1
while t:
    r+=(t%10)**x
    t//=10
    x-=1
print(r==t2 and "Disarium" or "Not Disarium number")

