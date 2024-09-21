import psycopg2
import os

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="Data_Processing_Bots",
    user="Thomas",
    password="JamesDeanBlue22!"
)
cur = conn.cursor()

def store_file(file_path):
    file_name = os.path.basename(file_path)
    with open(file_path, 'rb') as file:
        file_content = file.read()

    insert_query = """
    INSERT INTO public."Scraped_Data" (file_name, file_path, file_content)
    VALUES (%s, %s, %s)
    """
    cur.execute(insert_query, (file_name, file_path, file_content))
    conn.commit()
    print(f"File {file_name} stored successfully.")

# Example usage
store_file(r"C:\Users\mende\Documents\N Data_Processing_Bots\scraped_data.txt")

# Close the connection
cur.close()
conn.close()