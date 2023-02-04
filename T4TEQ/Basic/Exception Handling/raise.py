def div(x,y):
    print(x/y)

try:
    x,y=int(input()),int(input())
    if y==0:
        raise ValueError('Wrong')
    div(x,y)
except ValueError as e:
    print(e)
