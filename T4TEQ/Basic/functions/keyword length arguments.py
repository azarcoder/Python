#keyword length arguments
def demo(**n):
    print(n['fn'],n['ln'])

demo(fn="azaru",ln="deen")
#demo(fn="azar")#error
demo(ln="deen",fn="azaru")
