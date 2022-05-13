# This file is used to test the connection to the PostgreSql database by printing the version
import psycopg2
from config import config

def connect():
    conn = None
    try:
        # Read the connection parameters
        params = config()

        # Connect to postgre using the parameters
        print('Connection to the PostgreSQl database...')
        conn = psycopg2.connect(**params)

        # Create a cursor
        cur = conn.cursor()

        # Execute a statement
        print('PostgreSql version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)

        # Close postgre connection
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()