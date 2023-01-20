s=input()
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
t=ord(s[0])
for i in range(1,len(s)):
    t=gcd(t,ord(s[i]))
print(t)
