#jishan mahida
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="mydb"
)

mycursor = mydb.cursor()

sql = "DELETE FROM tbl_student WHERE st_id = 2"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "records deleted")
