import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3307,
    database ='azar'
)
mycursor = mydb.cursor()

n=input('Enter name:')
#normal
'''
sql = f"SELECT * FROM STUDENTS WHERE name='{n}'"
'''
#prevent SQL INJECTION
sql = f"SELECT * FROM STUDENTS WHERE name = %s "
name=n,
mycursor.execute(sql,name)
r = mycursor.fetchall()
for i in r:
    print(i)