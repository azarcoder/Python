t=tuple([i for i in input().split(',')])
d='';f='';s=''
for i in t:
    if i.isalpha():
        s+=i+','
    elif i.isdigit():
        d+=i+','
    else:
        f+=i+','
print(d.strip(','))
print(s.strip(','))
print(f.strip(','))
