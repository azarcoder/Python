class me():
    def __init__(self,n,a,c):#constructor function
        self.name=n
        self.age=a
        self.city=c
    def details(self):
        print("hi i am "+self.name+" from:"+self.city)

x=me('Azarudeen',21,'Trichy')
x.details()

        
