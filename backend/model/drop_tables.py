import psycopg2
from config import config

def drop_tables(schema='dropschema.sql'):
    conn = None
    try:
        schema_file = open(schema, 'r')
        commands = schema_file.read()

        # Read the connection parameters
        params = config()

        # Connect to postgre using the parameters
        conn = psycopg2.connect(**params)

        # Create a cursor
        cur = conn.cursor()

        # Execute the sql commands
        cur.execute(commands)

        # Close PostgreSql connection
        cur.close()

        # Commit changes
        conn.commit()
    except FileNotFoundError:
        print("File '{0}' not found.".format(schema))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print('Tables dropped successfully.')

if __name__ == '__main__':
    drop_tables()