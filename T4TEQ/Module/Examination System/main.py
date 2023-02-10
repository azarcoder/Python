import staffpage
import studentpage
while True:
    print('Enter As,')
    print('1.Staff\n2.Student\n3.Exit')
    n=int(input())
    try:
        if n==1:
            s=staffpage.Sf().staff_interface()
        if n==2:
            s=studentpage.St().student_interface()
        if n==3:
            break 
    except:
        print('Invalid input!')
