import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3307,
    database ='azar'
)
mycursor = mydb.cursor()

#LIMIT
# mycursor.execute('SELECT * FROM students LIMIT 3') #only print 3 data
#OFFSET
mycursor.execute('SELECT * FROM students LIMIT 5 OFFSET 2')#OFFSET - starting from given record
r = mycursor.fetchall()
for i in r:
    print(i)