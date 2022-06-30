#jishan mahida
import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    username= "root",
    password= "",
    database= "mydemo"
)

mycursor = mydb.cursor()

sql = " UPDATE tbl_user SET user_id = 'bhoot' WHERE user_id = '2'"


mycursor.execute(sql)


mydb.commit()

print(mycursor.rowcount, "row updated")
