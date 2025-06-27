import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

def create_database():
    """Creates alx_book_store database without using SELECT/SHOW"""
    connection = None
    try:
        # 1. Verify .env configuration
        if not os.path.exists('.env'):
            raise RuntimeError(".env file not found")
        if os.path.getsize('.env') == 0:
            raise RuntimeError(".env file is empty")
        
        # 2. Load credentials securely
        load_dotenv()
        
        # 3. Establish connection
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        
        # 4. Create database directly (no existence check via SELECT/SHOW)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        connection.commit()
        
        print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as e:
        print(f"MySQL Connection Error: {e}")
    except RuntimeError as e:
        print(f"Configuration Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
