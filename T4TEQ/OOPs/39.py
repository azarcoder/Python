class strop:
    def len():
        s='String Length'
        print("{:*^21}".format(s))
        n=input('Enter a string:')
        print(len(n))
    def rev():
        s='String Reverse'
        print("{:*^21}".format(s))
        n=input('Enter a string:')
        print(n[::-1])
    def cmp():
        s='String Compare'
        print("{:*^21}".format(s))
        n=input('Enter a first string:')
        n2=input('Enter a second string:')
        print(n==n2 and "same" or "not same")
    def vow_count():
        s='Vowel Count'
        print("{:*^20}".format(s))
        n=input('Enter a string:')
        c=0
        for i in n:
            if i in 'aeiouAEIOU':
                c+=1
        print(c)
    def zipper():
        s='String Zipper'
        print("{:*^20}".format(s))
        n=input('Enter a first string:')
        n2=input('Enter a second string:')
        x=zip(n,n2)
        print(dict(x))


strop.len()
strop.rev()
strop.cmp()
strop.vow_count()
strop.zipper()

