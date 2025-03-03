import pymysql
from pymysql import cursors

from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"), 
    "database": os.getenv("DB_NAME"),
    "cursorclass": cursors.DictCursor
}


def get_db_connection():
    """Crée et retourne une connexion à la base de données."""
    connection = pymysql.connect(**DB_CONFIG)
    return connection

connection = get_db_connection()
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"MySQL Version: {version}")
finally:
    connection.close()
