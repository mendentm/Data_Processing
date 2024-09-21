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

def retrieve_file(file_id, output_directory):
    select_query = """
    SELECT file_name, file_content FROM public."Analyzed_Data" WHERE id = %s
    """
    cur.execute(select_query, (file_id,))
    result = cur.fetchone()
    if result:
        file_name, file_content = result
        output_path = os.path.join(output_directory, file_name)  # Correct output path
        with open(output_path, 'wb') as file:
            file.write(file_content)
        print(f"File {file_name} retrieved successfully at {output_path}.")
    else:
        print("File not found.")

# Example usage, list the File ID and then the directory of where you want to file to go. 
retrieve_file(1, r"C:\Users\mende\Documents\Test")  

