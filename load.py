from dotenv import dotenv_values
from psycopg2.extensions import connection, cursor
import psycopg2

config = dotenv_values()

def get_connection() -> connection:
    """Establishes and returns a connection to the database."""
    conn = psycopg2.connect(
        dbname=config["DB_NAME"],
        user=config["DB_USER"],
        password=config["DB_PASSWORD"],
        host=config["DB_HOST"],
        port=config["DB_PORT"])
    return conn

def get_cursor(connection: connection) -> cursor:
    """Retrieves cursor from database connection"""
    cur = connection.cursor()
    return cur

if __name__ == "__main__":
    conn = get_connection()
    cur = get_cursor()
    