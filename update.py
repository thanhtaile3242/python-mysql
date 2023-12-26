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
        # Update a user's email by their username
        update_query = "UPDATE users SET email = %s WHERE username = %s"
        new_email = "thanhtaile3242@gmail.com"
        username = "Tai"

        mycursor.execute(update_query, (new_email, username))

        # Commit the changes to the database
        mydb.commit()
        print("Update successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()  # Rollback changes if an error occurs

    finally:
        # Close the cursor and connection
        mydb.close()

except mysql.connector.Error as err:
    print(f"Connection error: {err}")
