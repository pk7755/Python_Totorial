import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',passwd='root')
if conn.is_connected:
    print("connection established....")

myCursor = conn.cursor()
myCursor.execute('use mydb')


myCursor.execute(
    """
    
    CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
    """
)


