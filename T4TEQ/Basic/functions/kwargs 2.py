def demo(b,*n,**k):
    print(b)
    for i in n:
        print(i)
    for i in k.items():
        print(i)

demo('me','yes',fn="azar",ln="udeen")

