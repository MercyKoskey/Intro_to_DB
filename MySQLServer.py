#!/usr/bin/python3
"""Foolproof Database Creator"""

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import sys
import time

def log(message):
    """Ensure output appears immediately"""
    print(message, flush=True)
    time.sleep(0.1)  # Prevents output buffering issues

def create_database():
    try:
        log("\n=== STARTING DATABASE CREATION ===")
        
        # 1. Load environment variables (with explicit path)
        env_path = os.path.join(os.path.dirname(__file__), '.env')
        if not load_dotenv(env_path):
            log("⚠ WARNING: .env file not found in:\n" + env_path)
        
        # 2. Get credentials with validation
        required_vars = {
            'DB_HOST': 'localhost',
            'DB_USER': 'root', 
            'DB_PASSWORD': '',
            'DB_NAME': 'alx_book_store'
        }
        
        config = {}
        for var, default in required_vars.items():
            config[var.lower()] = os.getenv(var, default)
            log(f"{var}: {'*****' if 'PASSWORD' in var else config[var.lower()]}")
        
        # 3. Force MySQL connection (will error if fails)
        log("\nAttempting MySQL connection...")
        connection = mysql.connector.connect(
            host=config['db_host'],
            user=config['db_user'],
            password=config['db_password'],
            auth_plugin='mysql_native_password',
            connection_timeout=5  # Fail fast if can't connect
        )
        log("✔ MySQL connection successful")
        
        # 4. Create database
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config['db_name']}")
        log(f"✔ Database '{config['db_name']}' created/exists")
        
    except Exception as e:
        log(f"\n💥 CRITICAL ERROR: {type(e).__name__}")
        log(f"Message: {str(e)}")
        
        # Specific troubleshooting for common errors
        if isinstance(e, Error):
            if e.errno == 1045:
                log("\nSOLUTION: Check your MySQL password in .env file")
                log("Try resetting with:")
                log("ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new_password';")
            elif e.errno == 2003:
                log("\nSOLUTION: MySQL service not running")
                log("On Windows:")
                log("1. Press Win+R, type 'services.msc'")
                log("2. Find 'MySQL' and start it")
    finally:
        if 'connection' in locals():
            connection.close()
            log("Connection closed")
    
    input("\nPress Enter to exit...")  # Force window to stay open

if __name__ == "__main__":
    create_database()
    sys.exit(0)
