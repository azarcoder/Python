import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3307,
    database ='azar'
)
mycursor = mydb.cursor()

n=input('Enter name to delete data:')
#normal
'''
sql = f"DELETE FROM STUDENTS WHERE name='{n}'"
'''
#prevent SQL INJECTION
sql = f"DELETE FROM STUDENTS WHERE name = %s "
name=n,
mycursor.execute(sql,name)
print(mycursor.rowcount,'Deleted!')
mydb.commit()
mycursor.close()
mydb.close()
