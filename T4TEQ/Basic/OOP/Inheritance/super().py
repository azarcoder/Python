class parent:
    def display(self):
        print('parent')
class child(parent):
    def display(self):
        super().display()
        print('child')

t=child()
t.display()

#issubclass - check if subclass or not
print(issubclass(child,parent))
print(issubclass(parent,child))
a=child()
b=parent()
print(isinstance(a,child))
print(isinstance(a,parent))
print(isinstance(b,child))
print(isinstance(b,parent))

