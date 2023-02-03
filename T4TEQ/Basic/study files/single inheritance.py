#inheritance
#single
class A:
    def show (self):
        n='azar'
        print('t4teq',self.n)
class B(A):
        m='hi'
        def pr(self):
            print(self.m)
s=B()
s.pr()
s.show()
