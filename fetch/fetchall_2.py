# 2. Tìm kiếm tương đối (LIKE operator) 
# % (Percent Sign)
# Usage: Represents zero, one, or multiple characters.

# _ (Underscore Sign)
# Usage: Represents a single character.

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
        pattern = '_ohn%'
        query_statement = "SELECT * FROM users WHERE username LIKE %s"
        mycursor.execute(query_statement, (pattern,))  # Pass pattern as a tuple

        # Display the fetched results
        rows = mycursor.fetchall()
        if rows:
            for row in rows:
                print(row)
                # while mycursor.fetchall():
                #     pass 
        else:
            print("Not data")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    mydb.close()