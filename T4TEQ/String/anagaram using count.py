if len(a)==len(b):
    for i in a:
        if a.count(i)!=b.count(i):
            print("Not")
            break
    else:
        print("Anagram")
else:
    print("Not")
