class parent:
    def fun1(self):
        print('Parent 1')
class parent2:
    def fun2(self):
        print('Parent 2')
class parent3:
    def fun2(self):
        print('Parent 3')
class child(parent,parent2,parent3):
    def fun3(self):
        print('child')

t=child()
t.fun1()
t.fun2()
t.fun3()
print(child.__mro__) #it works based on method order passed
