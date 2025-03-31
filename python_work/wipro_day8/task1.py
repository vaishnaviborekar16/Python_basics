#Task 1: Create a Python script to connect to a MySQL database and fetch records from a table
import mysql.connector # type: ignore
host = "locahost"
user = "new_user01"
password = "Pas@123456"
database = "mydb1"

try:
    
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    
    cursor = conn.cursor()
    sql = "SELECT * FROM mydb1"
    cursor.execute(sql)
    rows = cursor.fetchall()

    
    for row in rows:
        print(row)

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")