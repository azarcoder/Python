import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3307,
    database ='azar'
)
mycursor = mydb.cursor()
s = input('Which you want to set?')
val = input("Enter value:")
id=int(input('Enter id:'))
sql = f"UPDATE students SET {s} ='{val}' WHERE id='{id}'"
mycursor.execute(sql)
print(mycursor.rowcount,'Updated!')
mydb.commit()

#prevent SQL INJECTION
#sql = f"UPDATE students SET {s} =%s WHERE id=%s"