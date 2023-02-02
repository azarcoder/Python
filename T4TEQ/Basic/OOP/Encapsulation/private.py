class demo:
    def __init__(self,n,a):
        self.__name = n
        self.__age = a
    def pp(self):
        print('Name:',self.__name)
        print('Age:',self.__age)
class demo2(demo):
    def pp2(self):
        print('Name 2:',self.__name)
        print('Age 2:',self.__age)

o = demo('Azar',21)
o.pp()
#print(o.name)#error

o2 = demo2('ameera',19)#error
o2.pp2()#error
'''
__ double underscore denotes private attribure

private:
Access from only own class
won't by derived class
won't by object

'''


