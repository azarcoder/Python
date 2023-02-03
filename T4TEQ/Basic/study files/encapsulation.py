#Encapsulation
class en:
    a=10
    _b=20
    __c=30
e=en()
print(e.a)
print(e._b)
print(e.__c)

#how to access private content:
class en:
    a=10
    _b=20
    __c=30
    def get(self):
        x=self.__c
        return x
e=en()
print(e.a)
print(e._b)
e.get()
