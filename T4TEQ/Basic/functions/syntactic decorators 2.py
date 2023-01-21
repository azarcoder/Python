#syntactic decorators
def pp(fn):
    def p():
        print("hi")
        fn()
        print("bye")
    return p

def ff(fn):
    def p():
        print("welcome")
        fn()
        print("close")
    return p

@ff
@pp
def me():
    print("azar")

me()
