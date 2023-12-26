# Import package MySQL Connector/Python
import mysql.connector
try:
    # Establish the connection to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password", # Insert password
        port="3306"
    )

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    try:
        # Create a new database
        mycursor.execute("CREATE DATABASE your_database")

        # Use the newly created database
        mycursor.execute("USE your_database")

        # Define the SQL statement to create the 'users' table within the database
        create_table_query = """
            CREATE TABLE users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL,
                gender ENUM('Male', 'Female', 'Other') NOT NULL
            )
        """

        # Execute the SQL statement to create the table
        mycursor.execute(create_table_query)

        # Commit the changes to the database
        mydb.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()  # Rollback changes if an error occurs
        
    finally:
        # Close the connection

        mydb.close()
except mysql.connector.Error as err:
    print(f"Connection error: {err}")



