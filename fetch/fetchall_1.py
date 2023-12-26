# Fetchall()
# Description: Retrieves all rows of a query result set and returns them as a list of tuples.
# Usage: Suitable when you want to retrieve and process all rows from the result set at once.
# Behavior: Returns an empty list if there are no rows in the result set.
# 1. Tìm kiếm tuyệt đối ( '=' OPERATOR)
import mysql.connector

try:
    # Establish the connection to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        port="3306",
        database="DBdemo2"  # Replace with your database name
    )

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    try:
        # Execute a SELECT query with a WHERE clause
        city_to_search = "New York"
        # 1.1 Basic query
        query_statement="SELECT * FROM users WHERE city = %s"

        # 1.2 Order by
        # query_statement="SELECT * FROM users WHERE city = %s ORDER BY username asc"

        # 1.3 Limit and Offset
        # query_statement="SELECT * FROM users WHERE city = %s ORDER BY email asc LIMIT 3 OFFSET 1"
        
        mycursor.execute( query_statement, (city_to_search,))

        # Fetch the results
        rows = mycursor.fetchall()
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
