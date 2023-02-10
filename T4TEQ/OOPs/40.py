try:
    a,b=[i for i in input().split()]
    if a.isdecimal() and b.isdecimal():
        print(int(a)+int(b))
    else:
        print(float(a)+float(b))
except:
    print(a+b)

