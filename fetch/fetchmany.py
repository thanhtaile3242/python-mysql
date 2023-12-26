import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        port="3306",
        database="DBdemo2"  # Replace with your database name
    )
    mycursor = mydb.cursor()
    try:
        city_to_search = "New York"
        query_statement = "SELECT * FROM users WHERE city = %s"
        mycursor.execute(query_statement, (city_to_search,))
        size = 3
        # Display the fetched results
        rows = mycursor.fetchmany(size)
        if rows:
            for row in rows:
                print(row)
        else:
            print("Not data")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    mydb.close()