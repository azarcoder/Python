class parent():
    def fun1(self):
        print('parent')
class child(parent):
    def fun2(self):
        print("child 1")
class child2(child):
    def fun3(self):
        print("child 2")

t1=child()
t2=child2()

t1.fun1()
t1.fun2()

t2.fun1()
t2.fun2()
t2.fun3()
