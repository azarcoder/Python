class global_var():
    id=1001
    name=[]
    mark=[]
    result=[]
    psw=[]
    roll=[]
    c=0
    attended=[]
class exam(global_var):
    def __init__(self):
        while True:
            print('Enter As,')
            print('1.Staff\n2.Student\n3.Exit')
            n=int(input())
            try:
                if n==1:
                    self.staff_main()
                if n==2:
                    self.student_interface();
                if n==3:
                    break 
            except:
                print('Invalid input!')
    #----------staff--------------------
    def staff_main(self):
        while True:
            print('1.Create Exam\n2.Student Report\n3.Approve\n4.Back to main')
            try:
                n=int(input())
                if n==1:
                    self.create_exam()
                if n==2:
                    self.report()
                if n==3:
                    self.approve() 
                if n==4:
                    break
            except:
                print('Invalid input!')
    
    def approve(self):
        if global_var.c==0:
            print("Student didn't registered yet")
        else:
            for i in range(global_var.c):
                if global_var.mark[i]>(len(self.d)//2) and global_var.attended[i]==1:
                    global_var.result[i]='pass'
                elif global_var.attended[i]==0:
                    global_var.result[i]='Not Evaluated'
                else:
                    global_var.result[i]='fail'
            for i in range(global_var.c):
                with open('data.txt','w') as f:#with automatically close the file
                    f.write(f'ID:{global_var.roll[i]} Name:{global_var.name[i]} mark:{global_var.mark[i]} Result:{global_var.result[i]}')
                    print("Student results approved successfully!")

    def report(self):
        for i in range(global_var.c):
            print(f'ID:{global_var.roll[i]} Name:{global_var.name[i]} mark:{global_var.mark[i]} Result:{global_var.result[i]}')

    def create_exam(self):
        n=int(input('Enter no of question:'))
        m=[]
        f=1
        self.d={}
        for i in range(n):
            print('Enter a questions:')
            x=[]
            q=input()
            x.append(q)
            print('Enter 4 options:')
            if f==1:
                print('[NOTE]=>option should be space seperated!')
                f=0
            y=[i for i in input().split()][:5]
            print('Enter correct answer:')
            cr=input()
            y.append(cr)
            x.extend(y)
            m.append(x)
            y.clear()
        for i in range(len(m)):
            q=m[0][i]
            a=m[i][1:]
            x={q:a}
            self.d.update(x)
        print('Questions created successfully!')
    #--------student-----------
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
    def register(self):
        global_var.roll.append(global_var.id)
        name=input('Enter your name:')
        global_var.name.append(name)
        password=input('Enter Password:')
        global_var.psw.append(password)
        mark=0
        global_var.mark.append(mark)
        result='Not Evaluated'
        global_var.result.append(result)
        print('Registered Successfully!')
        print('Your id:',global_var.id)
        global_var.attended.append(0)
        global_var.id+=1
        global_var.c+=1
    
    def login(self):
        eid=int(input('Enter ID:'))
        epass=input('Enter Password:')
        if eid in global_var.roll and epass in global_var.psw:
            print('login successful') 
            while True:
                print('1.Attend Exam\n2.Show result\n3.Logout')
                x=int(input())
                try:
                    if x==1:
                        self.attend_exam()
                        pass
                    if x==2:
                        self.show()
                        pass
                    if x==3:
                        break
                except:
                    print('Invalid input!!!')
        else:
            print("login error")
    
    def show(self):
        id=int(input("Enter your ID:"))
        print(f'Your id:{global_var.roll[(id%10)-1]} Result:{global_var.result[(id%10)-1]}')

    def attend_exam(self):
            id = int(input('Enter your ID:'))
            print('Welcome:',global_var.name[(id%10)-1]) #changed here self.reg to global_var.id
            if len(self.d)>0:
                for i in self.d:
                    print('Question:',i)
                    print('option')
                    print('------')
                    l=self.d[i]
                    op=1
                    for i in range(0,len(l)-1):
                        print(op,':',l[i])
                        op+=1
                    ch=input('Enter your answer:')
                    if ch==l[-1]:
                        global_var.mark[(id%10)-1]+=1
                global_var.attended[(id%10)-1]=1
                print('Exam completed Sucessfully! Thank You :)')
            else:
                print('Question Not created by Staff! Please visit again Later :)')

o = exam()
