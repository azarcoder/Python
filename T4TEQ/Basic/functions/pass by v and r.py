#pass by value - copy of arg (doesn't affect og)
n="positive"
def pbv(n):
    print(n)

pbv(n)
print(n)

#pass by reference - copy of arg (affect og)
m=[1,2,3,4]
def pbr(x):
    x.append(90)
    print(x)
pbr(m)
print(m)



    
