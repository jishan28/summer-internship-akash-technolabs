#jishan mahida
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="mydb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO tbl_student(st_name,st_email,st_mobile) VALUES ('jishan','jishanmahida880@gmail.com','9313919183')"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
