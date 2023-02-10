class global_var:
    id=101
    d={
        'US':[1001,'9:30 AM IST','1:00 PM IST','4:50 PM IST',120000,True],
        'UK':[1002,'4:50 AM IST','3:00 PM IST','3:30 PM IST',180000,True],
        'Canada':[1003,'3:30 AM IST','5:00 PM IST','2:30 PM IST',100000,True],
        'AU':[1004,'6:30 AM IST','7:00 PM IST','8:30 PM IST',98000,True],
        'Japan':[1005,'2:30 AM IST','9:00 PM IST','7:30 PM IST',42000,True],
        'Germany':[1006,'1:30 AM IST','12:00 PM IST','11:30 PM IST',230000,True],
    }
    approval=''
    passengers=[]
class flight(global_var):
    #----------------------main------------------------------
    def __init__(self):
        print('---Flight Reservation System---')
        while True:
            print('1.Passenger\n2.Cashier\n3.Exit')
            c=int(input())
            try:
                if c==1:
                    self.passenger()
                elif c==2:
                    self.cashier()
                else:
                    break
            except:
                print('Invalid input')
    
    #------------------passenger------------------------------
    def passenger(self):
        print('---Welcome Passenger---')
        while True:
            print('1.Sign in\n2.Login\n3.Exit')
            c=int(input())
            try:
                if c==1:
                    self.signup()
                elif c==2:
                    self.login()
                else:
                    break
            except:
                print('Invalid input')
    

    def signup(self):
        self.name = input('Enter your name:')
        self.psw = input('Enter Password:')
        self.id = global_var.id
        print(f'Registered successgully! Your id :{self.id}')
        global_var.id+=1
    
    def login(self):
        n = int(input('Enter Id:'))
        p =input('Enter password:')
        if n==self.id and p==self.psw:
            print('Welcome',self.name)
            while True:
                print('1.Check Availability & Fare\n2.Book Ticket\n3.Your flight Details\n4.Exit')
                c=int(input())
                try:
                    if c==1:
                        self.check()
                    elif c==2:
                        self.book()
                    elif c==3:
                        self.fdetails()
                    else:
                        break
                except:
                    print('Invalid input')

        else:
            print('No data found!')
    def fdetails(self):
        for i in global_var.passengers:
            if self.id == i:
                for i in global_var.d:
                    if global_var.d[i][-1]==False:
                        print(f'Name:{self.name} flight Timing:{global_var.d[self.cn][1]} Approval:{global_var.approval}')
                        break
            
    def check(self):
        self.go = input('Enter where you want to go?')
        self.s=[]
        for i in global_var.d:
            if i==self.go:
                self.s=global_var.d[i]
                break
        if len(self.s)==0:
            print('No Flight available for,',self.go)
        else:
            print('Flight Number:',self.s[0])
            for i in range(1,len(self.s)-2):
                print('Available:',self.s[i])
            print('Fare:',self.s[-2])
    

    def book(self):
        self.fno=int(input('Enter flight No:'))
        self.cn = input('Enter Country name:')
        for i in global_var.d:
            if i==self.cn:
                if  global_var.d[i][0] == self.fno and global_var.d[i][-1] == True:
                    global_var.d[i][-1]=False
                    global_var.passengers.append(self.id)
                    print('Ticket Booked Successfully!')
                    # print(global_var.d[i][-1])
                    break
            else:
                print('There is no flight avaliable right now!!!')
                break
            
        
    #-----------------------cashier-----------------------------
    def cashier(self):
        print('---Welcome Cashier---')
        while True:
            print('1.Approve\n2.Issue Ticket\n3.Exit')
            c=int(input())
            try:
                if c==1:
                    self.approve()
                elif c==2:
                    self.issue()
                else:
                    break
            except:
                print('Invalid input')
    
    def issue(self):
        for i in global_var.d:
            if global_var.d[i][-1]==False:
                print(global_var.d[i])
    def approve(self):
        for i in global_var.d:
            if global_var.d[i][-1]==False:
                global_var.approval='Approved'
        print('All passengers Approved Succesfully!')

o=flight()
