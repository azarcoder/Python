a,b=int(input()),int(input())
def div(a,b):
    return a/b
try:
    div(a,b)
except Exception as e:
    print(e)
else: #if exception doesn't occur, it will work otherwise work
    print('from else')
finally:
    print('process complete!')
    
