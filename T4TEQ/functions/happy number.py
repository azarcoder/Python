n=int(input())
def h(n):
    r=s=0
    while n:
        r=n%10
        s+=r*r
        n//=10
    return s

while(n!=1 and n!=4):
    n=h(n)
print("happy" if h(n)==1 else "not")

"""
n=19
82 68 100 1
"""

