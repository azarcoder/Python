"""
a b c d
e f g
h i
j
"""
a=97
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(a),end=" ")
        a+=1
    print()