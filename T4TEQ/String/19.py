n=input()
s=''
for i in range(len(n)):
    if n[i-1] not in 'aeiouAEIOU' :
        s+=n[i] 
print(s)
