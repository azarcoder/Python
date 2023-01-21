#syntactic decorators
def pp(fn):
    def p():
        print("hi")
        fn()
        print("bye")
    return p

@pp
def me():
    print("azar")

me()
