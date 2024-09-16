# Need to update 

# Possible Scraping functions:
def insert_scraped_data(connection, data):
    cursor = connection.cursor()
    insert_query = """
        INSERT INTO scraped_data (url, content, scraped_on)
        VALUES (%s, %s, NOW())
    """
    cursor.execute(insert_query, (data['url'], data['content']))
    connection.commit()
    cursor.close()
    print("Data inserted successfully!")

# Possible Data Analysis functions:
def fetch_data_for_analysis(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM scraped_data WHERE analyzed = FALSE")
    results = cursor.fetchall()
    cursor.close()
    return results

# Closing the connection
def close_connection(connection):
    if connection is not None:
        connection.close()
        print("Database connection closed.")
