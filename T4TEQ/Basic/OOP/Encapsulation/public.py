class demo:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def pp(self):
        print('Name:',self.name)
        print('Age:',self.age)
class demo2(demo):
    def pp2(self):
        print('Name2:',self.name)
        print('Age2:',self.age)

o = demo('Azarudeen',21)
o2 = demo2('t4teq',7)
print(o.name)
print(o.age)
o.pp()
o2.pp2()
#public can access from own class,derived class and from object
