def demo(*n):
    print(n)
    print(*n)
    for i in n:
        print(i)

demo('a','b','d','e',12)
