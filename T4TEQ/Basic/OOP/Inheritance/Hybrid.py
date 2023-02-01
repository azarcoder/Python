class parent1():
    def fun1(self):
        print('parent')
class parent2(parent1):
    def fun2(self):
        print("child 1")
class child1(parent1):
    def fun3(self):
        print("child 2")
class child2(child1,parent2):
    def fun4(self):
        print("child 2")

t1=child1()
t2=child2()

t1.fun1()
t1.fun3()

t2.fun1()
t2.fun2()
t2.fun3()
