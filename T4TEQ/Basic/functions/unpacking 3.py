#unpacking 3
t= (1,2,3,4,5)
def mm(*n):
    t=0
    for i in n:
        t+=i
    return t
print(mm(*t))
x=[1,5,3,1]
print(mm(*x))
