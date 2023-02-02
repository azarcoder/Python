d={
    1:"azar",
    2:"deen",
    4:"trichy",
    3:21
    }
k = list(d.keys())
k.sort()
s={i : d[i] for i in k} #sort based on key
print(s)
