s='azaR'

#capitalize() - first char to Upper
print('capitalize=>',s.capitalize())

#upper - to uppercase
print('upper=>',s.upper())

#casefold - to lowercase
print('casefold=>',s.casefold())

g='azaru deen welcome to t4teq'
#title - first char of each word to uppercase
print('tilte=>',g.title())

#center (len,char) - centered str
print('center=>',s.center(6,'*'))

#count (val,start,end) - return count
print('count=>',s.count('a'))

#endswith(val,start,end)
print('endswith=>',s.endswith('R'))

#stratswith(val,start,end)
print('startswith=>',s.startswith('R'))

#find(val,s,e)
'''
first occurence
return index
if not found ***return -1*** 
'''
print('find',s.find('a'))

#find(val,s,e)
'''
last occurence
return index(last)
if not found ***return -1*** 
'''
print('rfind:',s.rfind('a'))

#index(val,s,e)
'''
first occurence
return index
if not found ***return error***
'''
print('index',s.index('a'))

#rindex(val,s,e)
'''
last occurence
return index
if not found ***return error***
'''
print('rindex',s.rindex('a'))

#isalnum() - alphanumberic ( space not allowed )
#isalpha() - only alphabet
#isdecimal() - only decimal
#digit() - accept fraction,numbers
#isidentifier() - variable rule
#islower()
#isupper()
#isprintable() - \n \t not printable so false
#isspace()
#istitle() - True if first character uppercase in each word


#join(iterable) - add end of the iterable
me='________'
a='X'.join(me)
print('join=>',a)

#rjust(lenght,char) - right justified
k='azar'
print('rjust=>',k.rjust(8,'*'))

#ljust(lenght,char) - left justofied
k='azar'
print('ljust=>',k.ljust(8,'*'))

#strip - remove white spaces
l='   asdf'
print('left strip=>',l.lstrip())
r='   asdf    '
print('right strip=>',r.rstrip())

#partition(value) - returns tuple where the string is parted into three parts

t='azaru deen'
o=t.partition('e') 
print('partition=>',o)#('azaru d', 'e', 'en')

#rpartition(value) - returns tuple where the string is parted into three parts

t='azaru deen'
o=t.rpartition('e') 
print('rpartition=>',o)#('azaru de', 'e', 'n')

#replace (old value,new value,count) - doesn't affect og we have store in another variable
e=t.replace('a','m')
print('replace=>',e)

#split(seperator,len) - converts into list
x='a b cat dog'
print(x.split()) #split by space
#rsplit() - left split()

f='wow\nTAmil\nAza\nman\nFuck'
print('swap cases=>',f.swapcase())
x=f.splitlines()
print('split lines=>',x)

#zfill(len) - fill zero till len (at the begining)
c='azar'
print(c.zfill(10))#000000azar



