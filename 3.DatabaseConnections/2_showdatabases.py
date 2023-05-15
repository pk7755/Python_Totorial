
import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',passwd='root')
if conn.is_connected:
    print("connection established....")

mycursor = conn.cursor()

mycursor.execute('show databases')

for i in mycursor:
    print(i)


