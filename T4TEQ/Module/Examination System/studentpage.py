from staffpage import Sf
class global_var():
    id=1001
    name=''
    mark=0
    result=''
    psw=''
class St(global_var):

    #exam attend
    def attend_exam(self):
        print('Welcome:',global_var.id) #changed here self.reg to global_var.id
        if len(Sf.d)>0:
            for i in Sf.d:
                print('Question:',i)
                print('option')
                print('------')
                l=Sf.d[i]
                op=1
                for i in range(0,len(l)-1):
                    print(op,':',l[i])
                    op+=1
                ch=input('Enter your answer:')
                if ch==l[-1]:
                    #self.mark+=1 #changed
                    global_var.mark+=1
            print('Exam completed Sucessfully! Thank You :)')
            # global_var.mark=self.mark
        else:
            print('Question Not created by Staff! Please visit again Later :)')
        
    #registeration    
    def register(self):
        self.reg=global_var.id
        self.name=input('Enter your name:')
        global_var.name=self.name
        self.password=input('Enter Password:')
        global_var.psw=self.password
        self.mark=0
        global_var.mark=self.mark
        self.result='Not Evaluated'
        print('Registered Successfully!')
        print('Your id:',self.reg)
        # global_var.id+=1
    
    #login
    def login(self):
        self.eid=int(input('Enter ID:'))
        self.epass=input('Enter Password:')
        if self.eid==global_var.id and self.epass==global_var.psw:
            print('login successful') 
            while True:
                print('1.Attend Exam\n2.Show Details\n3.Logout')
                x=int(input())
                try:
                    if x==1:
                        self.attend_exam()
                    if x==2:
                        self.show()
                    if x==3:
                        break
                except:
                    print('Invalid input!!!')
        else:
            print("login error")
    
    #show details
    def show(self):
        print(f'Your id:{global_var.id} Result:{global_var.result}')
    

    #interface
    def student_interface(self):
        while True:
            print('----Welcome to Student Page----')
            print('1.Register\n2.Login\n3.Back to main')
            n=int(input())
            try:
                if n==1:
                    self.register()
                if n==2:
                    self.login()
                if n==3:
                    break
            except:
                print('Invalid input:(')

