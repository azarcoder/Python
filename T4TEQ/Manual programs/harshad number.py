a=int(input());t=a
r=0
while a:
    r+=a%10
    a//=10
if(t%r==0):
    print("Harshad")
else:
    print("Not Harshad")
