#jishan mahida
import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    username= "root",
    password= "",
    database= "mydemo"
)

mycursor = mydb.cursor()

sql = "INSERT INTO tbl_user(user_id,user_firstname,user_lastname,user_address,user_email,user_password) VALUES('001','jishan','mahida','gujarat','jishanmahida880@gmail.com','280901')"
sql = "INSERT INTO tbl_user(user_id,user_firstname,user_lastname,user_address,user_email,user_password) VALUES('002','shan','xyz','delhi','shanmahida880@gmail.com','280901')"
sql = "INSERT INTO tbl_user(user_id,user_firstname,user_lastname,user_address,user_email,user_password) VALUES('003','ishan','abc','goa','ishanmahida880@gmail.com','280901')"

mycursor.execute(sql)
mycursor.execute(sql)
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "row inserted")
