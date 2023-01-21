import functools

'''
lambda - function without name
return only one value at end
'''
'''
n,y=int(input()),int(input())
s = lambda x:x*2
m = lambda x,y:x*y
print(s(n),m(n,y))
'''
#with map,filter,reduce

#filter - used to filter the list
l=[12,2,34,5,6,7]
op = list(filter((lambda x: x%2==0),l))
print(op)

#map - used to modify item in the list
mop = list(map((lambda x:x*x),l))
print(mop)

'''
#reduce - we need to import functools
mg=[1,2,3,4,5]
r = list(reduce((lambda x,y:x+y),mg))
print(r)
'''


