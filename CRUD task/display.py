#jishan mahida
import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    username= "root",
    password= "",
    database= "mydemo"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM tbl_user")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
