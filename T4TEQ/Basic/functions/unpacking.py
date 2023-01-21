#unpacking
m=[1,2,'me',56]
print(m)
print(*m)

#unpacking dictionary

d =  {
    'name':'Azar',
    'age' : '21',
    'city' : 'Tiruchirappalli'
    }
print(d)
print(*d)#only return key
m={**d}
print(m)



