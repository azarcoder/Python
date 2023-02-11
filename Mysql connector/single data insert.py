import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3307,
    database="azarpython"
)
mycursor = mydb.cursor()

l=[]
id=int(input('Enter ID:'))
name = input('Enter name:')
psw = input('Enter password:')
l.append(id)
l.append(name)
l.append(psw)
val=tuple(l)

try:
    sql ="INSERT INTO STUDENTS(id,name,password) VALUES (%s,%s,%s)"
    mycursor.execute(sql,val)
    print('Data inserted successfull!')
    mydb.commit()
except:
    print('Error while insertion!')

mycursor.close()
mydb.close()
