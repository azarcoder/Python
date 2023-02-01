class grandparent:
    def fun1(self):
        print('Grandparents')
class parent(grandparent):
    def fun2(self):
        print('parent')
class child(parent):
    def fun3(self):
        print("child")

t=child()
t.fun1()
t.fun2()
t.fun3()
