#jishan mahida
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="mydb"
)

mycursor = mydb.cursor()

sql = "UPDATE tbl_student SET st_name ='dharam' WHERE st_id = 3"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record updated.")
