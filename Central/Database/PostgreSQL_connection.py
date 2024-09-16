import psycopg2
from configparser import ConfigParser

# Load configuration from the .ini file
def config(filename='db_config.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db_params = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_params[param[0]] = param[1]
    return db_params

# Connect to PostgreSQL
def connect():
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        print("Connection to the PostgreSQL database successful!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    return connection
