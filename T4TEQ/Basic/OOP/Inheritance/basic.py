class parent:
    def fun1(self):
        print('Parent')
class child(parent):
    def fun2(self):
        print('child')

t=child()
t.fun1()
t.fun2()
