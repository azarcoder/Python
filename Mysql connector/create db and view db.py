import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3307
)
mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)
#mycursor.execute("CREATE DATABASE pydb")

d= input("Enter database name:")
try:
    mycursor.execute(f"CREATE DATABASE {d}") 
    print('Database created successfully')
except:
    print('Database aleready Exist')




