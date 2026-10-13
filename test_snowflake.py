from src.snowflake_connection import get_snowflake_connection
try:
    connection = get_snowflake_connection() 
    print("Snowflake connection successful!")
    cursor = connection.cursor() 
    cursor.execute("SELECT COUNT(*) FROM SALES_DATA") 
    result = cursor.fetchone() 
    print("Total rows in Snowflake:", result[0]) 
    cursor.close() 
    connection.close() 
except Exception as error: print("Connection failed:", error)