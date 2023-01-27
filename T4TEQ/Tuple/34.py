n=tuple(["{:b}".format(int(i)) for i in input().split(',')])
'''s=list(n)
def btod(n):
    r=0;j=1
    while n:
        r+=(n%2)*j
        j*=10
        n//=2
    return r
s=''
for i in n:
    s+=str(btod(i))+","

print(s.strip(','))'''
print(*n,sep=",")
    

    
        
