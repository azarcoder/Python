import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3307,
    database="azar"
)
c = mydb.cursor()
sql = "SELECT * FROM STUDENTS ORDER BY name" #by default ascending
# sql = "SELECT * FROM STUDENTS ORDER BY name DESC" #decending
c.execute(sql)
r=c.fetchall()
for i in r:
    id,name,password=i
    print(f'ID:{id} NAME:{name} PASSWORD:{password}')
