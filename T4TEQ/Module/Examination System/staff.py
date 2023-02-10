import main
class Staff:
    def __init__(self):
        while True:
            name = input('Enter name:')
            id = input('Enter ID:')
            if name=='azar' and id=='1234': 
                while True:
                    s="STAFF PAGE"
                    print(s.center(40,'*'))
                    print('1.Approve Students\n2.Create Exams & Generate Report file\n3.Exit from Staff page')
                    n=int(input())
                    try:
                        if n==1:
                            pass
                        elif n==2:
                            pass
                        elif n==3:
                            s=main() 
                    except:
                        print('Enter correct input!')
            else:
              print('invalid name or id')
