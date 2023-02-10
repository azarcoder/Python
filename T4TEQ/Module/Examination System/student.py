class Student:
    def login():
        print('login page')
    def signup():
        print('signup page')
    def __init__(self):
        while True:
            print('1.SignUp\n2.Login\n3.Exit from student')
            n=int(input('Enter choice:'))
            try:
                if n==1:
                    signup()
                elif n==2:
                    login()
                elif n==3:
                    s=main()   
            except Error as e:
                print(e)
