import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (adjust user, password, host as needed)
        connection = mysql.connector.connect(
            user='root',
            password='your_password',
            host='localhost'
        )

        cursor = connection.cursor()

        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Clean up: close cursor and connection if they exist
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
