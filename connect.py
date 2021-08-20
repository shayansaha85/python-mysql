import mysql.connector
import os

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Shayan97@",
database="sql_store"
)
print("CONNECTED....")
print("OBJECT : ",mydb)
cursor = mydb.cursor()
cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()
s = ""
for x in result:
    s = s+str(x)+"\n"
file = open("customers_table.txt", "w")
s = s.replace("(","")
s = s.replace(")","")
file.write(s)
file.close()
print("File saved...")