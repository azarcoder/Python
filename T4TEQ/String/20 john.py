a=input()
m='';n=0
for i in a:
    if i not in m and i.swapcase() not in m and i.isalpha():
        m+=i
        x=a.lower().count(i.lower())
        if x>n:
            n=x
            c=i
        print(i+'-'+str(x),end=' ')
print('\n'+c)
