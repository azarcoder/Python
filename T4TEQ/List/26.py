s=input()
l=[];e=''
n=int(input())
t=n
for i in range(n):
    e+=s[i::n]
    l.append(e)
    e=''
print(l)
        
    
