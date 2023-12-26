import mysql.connector

try:
    # Establish the connection to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        port="3306",
        database="DBdemo2"  # Connect to the 'LTT' database
    )

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    try:
        # Fetch all table names in the 'LTT' database
        mycursor.execute("DROP TABLE products")

        print("Drop table successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        mydb.close()

except mysql.connector.Error as err:
    print(f"Connection error: {err}")
