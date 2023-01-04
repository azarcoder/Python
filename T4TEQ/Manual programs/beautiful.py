a=int(input())
r=0
while a:
    r+=(a%10)**2
    a//=10
if(r**0.5==int(r**0.5)):
    print("Beautiful")
else:
    print("Not beautiful")
