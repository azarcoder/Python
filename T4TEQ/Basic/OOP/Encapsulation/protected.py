class demo:
    def __init__(self,n,a):
        self._name = n
        self._age = a
    def pp(self):
        print('Name:',self._name)
        print('Age:',self._age)
class demo2(demo):
    def pp2(self):
        print('Name 2:',self._name)
        print('Age 2:',self._age)

o = demo('Azar',21)
o.pp()

o2 = demo2('ameera',18)
o2.pp2()

#print(o2.name)#error
print(o2._name)#mangling access

'''
_ single underscore denotes mangling access privare members

Protected:
Access from  own class
Access by derived class
won't by object
'''


