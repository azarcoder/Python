s=input()
#print(sorted(s)) returns as list
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]>s[j]:
            s=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
print(s)
