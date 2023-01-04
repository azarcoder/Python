a=int(input())
f=False
for i in range(2,a//2+1):
    if(a%i==0):
        print("Not prime palindrome")
        break
else:
    r=0;t=a
    while(a):
        r=r*10+a%10
        a//=10
    if(r==t):
        print("Prime palindrome")
    else:
        print("Not prime palindrome") 
        