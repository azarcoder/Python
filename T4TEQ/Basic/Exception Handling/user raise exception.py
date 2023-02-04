def div(a,b):
    return a/b
try:
    a,b=int(input()),int(input())
    if b==0: #if is this true, it won't execute below
        raise ValueError("0 vaala divide panna mudiyathuda paithiyamey:)")
    print(div(a,b))
except ValueError as e:
    print(e)
finally:
    print('process complete!')
    
