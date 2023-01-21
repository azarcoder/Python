#decorators - decorators are function as arguments in another function
'''
it's called Meta Programming
'''
def ff(me):
    def p():
        print("hi")
        me()
        print("bye")
    return p

def cc():
    print("azar")

s=ff(cc)
s()
    
