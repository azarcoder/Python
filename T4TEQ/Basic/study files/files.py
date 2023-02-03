#f=open('testfile.txt','rt')
#print(f.read())

'''
#if the file in other location
s=open('A:\myfiles\exfile.txt','r')
print(s.read())
'''

#print(f.read(8)) #Return the 5 first characters of the file

'''
print(f.readline())#print only one line
print(f.readline()) #it's print second line of that file
'''

'''
#loop:
for i in f:
    print(i) #this prints line by line
'''

'''
#close files
f.close() #Close the file when you are finish with it
'''

'''
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
'''

#create the file
#t=open('newfile.txt','x')
'''
#append contend in file
f=open('newfile.txt','a')
f.write('now this file have one line')
f.close()

#open and read the file after the appending:
f=open('newfile.txt','r')
print(f.read())
'''

'''
#overwrite the content
f=open('newfile.txt','w')
f.write('I changed the line one')
f.close()

#after overwrite
f=open('newfile.txt','r')
print(f.read())
'''

'''
#remove file
import os
os.remove('newfile.txt')
'''

'''
#Check if file exist:
import os
if os.path.exists('TESTFILE.TXT'): #if file name is caps its also delete file correctly without errors
    os.remove('TESTFILE.TXT')
else:
    print('file not exists')

'''

'''
#delete folder -only delete empty folders
import os
os.rmdir("file handle")
'''
