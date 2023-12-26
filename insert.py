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
        # Define the SQL statement to insert data into the 'users' table
        insert_query = """
            INSERT INTO users (username, email, gender)
            VALUES (%s, %s, %s)
        """

        # Data to be inserted into the 'users' table
        user_data = [
            ("John", "john@gmail.com", "Male"),
            ("Emma", "emma@gmail.com", "Female"),
            ("Alex", "alex@gmail.com", "Other"),
            ("Tai", "tai@gmail.com", "Other"),
            ("Phuc", "phuc@gmail.com", "Male"),
            ("Truc", "truc@gmail.com", "Female"),
        ]

        # Execute the insert query for each user in user_data
        mycursor.executemany(insert_query, user_data)

        # Commit the changes to the database
        mydb.commit()
        print("insert data successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()  # Rollback changes if an error occurs

    finally:
        # Close the connection
        mydb.close()

except mysql.connector.Error as err:
    print(f"Connection error: {err}")
