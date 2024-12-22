# test_connection.py
from config import DB_CONFIG
import psycopg2

def test_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_CONFIG['database'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port']
        )
        print("Successfully connected to the database!")
        
        # Test a simple query
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM shipments;")
        count = cur.fetchone()[0]
        print(f"Number of shipments in database: {count}")
        
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_db_connection()