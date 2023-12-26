import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        port="3306",
        database="DBdemo2"
    )

    mycursor = mydb.cursor()
    city_to_search = "New York"
    query_statement = "SELECT * FROM users WHERE city = %s"
    mycursor.execute(query_statement, (city_to_search,))

    row = mycursor.fetchone()
    if row:
        print(row)
    else:
        print("No data")
   
except mysql.connector.Error as err:
    print(f"Connection error: {err}")
finally:
    mydb.close()

   