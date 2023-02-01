'''
property() - like set ,get ,delete
'''
class hi:
    def __init__(self):
        self.name='Azar'
    def set_name(self,name):
        self.__name=name #setting value
    def get_name(self):
        return self.__name #getting value
    #creating property object
    name = property(get_name,set_name)
o = hi()
#o.name='Azarudeen'
print(o.name)
        
