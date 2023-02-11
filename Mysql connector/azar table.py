import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3307,
    database ='azar'
)
mycursor = mydb.cursor()

try:
    mycursor.execute("""
    CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    password VARCHAR(255)
    );
""")
    print("Table created!")

except:
    print("Table already Exist!")