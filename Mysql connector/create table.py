import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3307,
    database="azarpython"
)
mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE TABLE STUDENTS(id INT NOT NULL,name VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL)")
    print("Table created")
    mycursor.execute('SHOW TABLES')
    for x in mycursor:
        print(x)
except:
    print("Table already exist")

#mycursor.execute("ALTER TABLE STUDENT ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")