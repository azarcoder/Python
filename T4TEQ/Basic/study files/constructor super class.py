#constructor
class a:
    def __init__(self):
        print('azar')
class b:
    def __init__(self):
        print('hello')
        super().__init__() #super() - it calls parent class
one=a()
two=b()
