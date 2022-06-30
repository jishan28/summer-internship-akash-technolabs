#jishan mahida
import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    username= "root",
    password= "",
    database= "mydemo"
)

mycursor = mydb.cursor()

sql = "DELETE FROM tbl_user WHERE user_id = 3"


mycursor.execute(sql)


mydb.commit()

print(mycursor.rowcount, "row deleted")
