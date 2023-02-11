import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3307,
    database ='azar'
)
mycursor = mydb.cursor()

n=int(input('Enter no of student you want to insert:'))
val=[]
for i in range(n):
    t=None,input('Enter name:'),input('Enter Password:')
    val.append(t)
try:
    sql = "INSERT INTO STUDENTS(id,name,password)  VALUES(%s,%s,%s)"
    mycursor.executemany(sql,val)
    mydb.commit()
    print(mycursor.rowcount,'inserted successfully!')
except:
    print('error while insertion!')
