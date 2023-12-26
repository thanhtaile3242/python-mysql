import mysql.connector

try:
    # Establish the connection to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        port="3306",
        database="DBdemo2"  
    )

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    try:
        # Execute a SELECT query with a WHERE clause
        query_statement= """
        SELECT u.username, sum(p.amount)  FROM users u JOIN payment p on u.id = p.user_id GROUP BY u.username;
        """
        mycursor.execute(query_statement)  # Pass pattern as a tuple

        # Fetch the results
        result = mycursor.fetchone()

        # Display the fetched results
        while result:
            print(result)
            result = mycursor.fetchone()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        mydb.close()

except mysql.connector.Error as err:
    print(f"Connection error: {err}")
