
class Sf:
    d={}

    # Approve
    def approve(self):
        from studentpage import global_var
        if global_var.mark==0:
            print("Student didn't attend exam yet!")
        else:
            if global_var.mark>global_var.mark//2:
                global_var.result='pass'
            else:
                global_var.result='fail'
            with open('data.txt','w') as f:#with automatically close the file
                    f.write(f'ID:{global_var.id} Name:{global_var.name} mark:{global_var.mark} Result:{global_var.result}')
            print("Student results approved successfully!")
    
    #report
    def report(self):
        from studentpage import global_var
        print(f'ID:{global_var.id} Name:{global_var.name} mark:{global_var.mark} Result:{global_var.result}')
        pass

    #interface 
    def staff_interface(self):
        while True:
            print('----Welcome to Staff Page----')
            n=input('Enter ID:')
            p=input('Enter Password:')
            b=input('if you want to go back, press [Y/y] or press[N/n]:')
            if b=='y' or b=='y'.upper():
                break
            else:
                try:
                    if n=='azar' and p=='123':
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
                    else:
                        print('Invalid ID/Password')
                except:
                    print('Invalid input!')
    
    #Exam creation
    def create_exam(self):
        n=int(input('Enter no of question:'))
        m=[]
        f=1
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