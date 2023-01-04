n=int(input())
def bo(n):
    p=1;s=0;j=1;z=0
    """binary to octal"""
    while n:
        s+=n%10*p
        p*=2
        n//=10
    while s:
        d=s%8
        z+=d*j 
        j*=10
        s//=8
    return z
    
    

print(bo(n))        
