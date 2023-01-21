#generator - returns an iteratable generator object

def demo():
    i=1
    while i<=5:
        yield i
        i+=1

r=demo()
print(r)#<generator object demo at 0x0000019EFBB3CDC0>
print(demo())##<generator object demo at 0x0000019EFBB3CDC0>
print(next(r))#1
print(next(r))#2
for i in r:
  print(i)


