try:
    a,b=int(input()),int(input())
    print(a/b)
except ValueError:
    print('value error')
except ZeroDivisionError:
    print('zero div error')
else:
    print('There is no exception in try block')
finally:
    print('process complete!')
    
