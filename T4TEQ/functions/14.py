n=int(input())

def pm(n):
    f=True
    if n==1:
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            f=False
            break 
    return f
        
def spl(n):
    f=False
    for i in range(1,n//2+1):
        if(pm(i) and pm(n-i)):
            f=True
            break
    return f
print(spl(n))

            
            
