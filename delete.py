import mysql.connector

try:
    # Establish the connection to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        port="3306",
         database="DBdemo1"  # Connect to the 'DBdemo1' database
    )

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    try:
        # Delete a user by their username
        delete_query = "DELETE FROM users WHERE username = %s"
        username = "Phuc"

        mycursor.execute(delete_query, (username,))

        # Commit the changes to the database
        mydb.commit()
        print("Delete successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()  # Rollback changes if an error occurs

    finally:
        # Close the cursor and connection
        mydb.close()

except mysql.connector.Error as err:
    print(f"Connection error: {err}")
