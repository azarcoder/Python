n,r=int(input()),int(input())
def rm(n,r):
    s=0;j=1
    while n:
        if n%10==r:
            n//=10
            continue
        else:
            s+=(n%10)*j 
        j*=10
        n//=10
    return s
print(rm(n,r))
