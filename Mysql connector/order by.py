import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3307,
    database ='azar'
)
mycursor = mydb.cursor()
sql = "SELECT * FROM students ORDER BY name"
mycursor.execute(sql)
r=mycursor.fetchall()
for i in r:
    id,n,p=i
    print(f'Id:{id}\tName:{n}\tPassword:{p}')
