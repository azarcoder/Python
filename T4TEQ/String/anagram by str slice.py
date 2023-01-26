a,b=input(),input()
def st(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]>s[j]:
                s=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
    return s
print(st(a)==st(b) and "anagram" or "not")
