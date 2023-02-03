'''What is list?
          list is a collection which is ordered and changable.In python list are written with square brackets'''
#list methods
#1.Add items-append()
#2.Remove items-remove(),pop(),del(),clear()
#3.copy items-copy(),list()
#4.join to list
#5.list count(),sort(),reverse()
#6.index(),extend(),Add any iterable 
#.7.Check if items exits
#8.change item values
#9.insert()
#10.loop through list
#***************************************************************************************************************#
'''1.Add items-append()'''

#1.append():
friends=['arthi','aanthiya','abdul','balaji','bala vivetha']
friends.append("azar")
print(friends)

'''2.Remove items-remove(),pop(),del(),clear()'''

#remove():#remove specified item
friends=['arthi','aanthiya','abdul','balaji','bala vivetha']
friends.remove("aanthiya")
print(friends)

#remove specified index
friends=['arthi','aanthiya','abdul','balaji','bala vivetha']
friends.pop(1)
print(friends)

#pop():(#pop deleted last items only)
friends=['arthi','aanthiya','abdul','balaji','bala vivetha']
friends.pop()
print(friends)

#del():
friends=['arthi','aanthiya','abdul','balaji','bala vivetha']
del friends[2]
print(friends)

#del keyword can also delete the list completely
del friends

#clear():(#This function cleared all of elements in the list)
friends=['arthi','aanthiya','abdul','balaji','bala vivetha']
friends.clear()
print(friends)

'''3.copy items-copy(),list()'''

#copy():
friends=['arthi','aanthiya','abdul','balaji','bala vivetha']
myfrds=friends.copy()
print(friends)
print(myfrds)

#list():
friends=['arthi','aanthiya','abdul','balaji','bala vivetha','azar']
myfrds=list(friends)
print(friends)
print(myfrds)

friends=list(("azar","abdul","balaji","arthi"))
print(friends)

'''4.join two list'''

#This is called list concadination
list1=['azar','arthi','balaji']
list2=['aanthiya','abdul','bala vivetha']
list3=list1+list2
print(list3)

'''5.List count(),sort(),reverse()'''

#count():(count a separate element how much time inside the list)
friends=['arthi','arthi','aanthiya','abdul','balaji','bala vivetha']
count=friends.count("arthi")
print(count)

#sort():
#This sorting in ACENDING order
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
friends.sort()
print(friends)

#This sorting in DECENDING order
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
friends.sort(reverse=True)
print(friends)

#reverse():
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
friends.reverse()
print(friends)

'''6.index(),extend(),Access items'''

#index():
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
index=friends.index("azar")
print(index)

#Access items in list:
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
print(friends[1])

#index -1 refers last item of the list,-2 is second last and -3 is thrid last
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
print(friends[-1])

friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
print(friends[-3])

#range of the index

friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
print(friends[1:4]) #1 is starting 4 is run till 3 because every last range is end-1

friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
print(friends[:4]) #this starts index 0 to end

friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
print(friends[2:]) #this starts index 2 to end
	
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
print(friends[-4:-2]) #this starts index -4 to -2

#extend():
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
friends2=['nithish','dinesh','daisy','chandru','giri']
friends.extend(friends2)
print(friends)

#add any iterable
'''the extend method does not have to append lists.you can add any iterable object (tuples,sets,dictionaries etc)
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
friends2=('bilal','faisal','boys')
friends.extend(friends2)
print(friends)

'''7.Check if items exits'''
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
if 'azar' in friends:
    print('yes')
else:
    print('not')

'''8.change item values'''
#change the value refer to index number
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
friends[1]='azarudeen'
print(friends)

#change range of items
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
friends[1:3]=['azar','bilal']
print(friends)

'''9.Insert()'''
#insert()-insert item method inserts an item at the specific index
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
friends.insert(2,'faisal')
print(friends)

'''10.loop through list'''
#print all items in the list one by one:
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
for x in friends:
    print(x)
#loop through index number
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
for i in range(len(friends)):
    print(friends[i])

#using while loop
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
i=0
while i < len(friends):
    print(friends[i])
    i+=1

#list comprehension
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
[print(i) for i in friends]

#append new list 
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
new_friends=[]
for i in friends:
    new_friends.append(i)
print(new_friends)

#another method one line codr:
'''syntax:
new_friends=[expression for item in iterable if condition == True)'''

friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
new_friends=[i for i in friends if 'a' in i]
print(new_friends)

#condition
'''this condition if i!='azar' will return True for all element other than
   'azar',making the new list contain all friends except 'azar' 

friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
new_friends=[i for i in friends if i !='azar']

#with no if statement:
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
new_friends=[x for x in friends]
print(new_friends)

#range() #it's gives output like index value 
friends=['arthi','azar','aanthiya','abdul','balaji','bala vivetha']
new_friends=[i for i in range(4)]
print(new_friends)
#condition accepted!!!
new_friends=[i for i in range(5) if i <3] #this ouput is <3 so output till range 3! o/p: [0,1,2]

#expression
new_friends=[i.upper() for i in friends] #upper represent upper case value

new_friends=['hello' for i in friends] #set all values in the new list to 'hello'

new_friends=[i if i !='arthi' else 'azar' for i in friends] #return item it is not arthi ,if it is aarthi return azar. 