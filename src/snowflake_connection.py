import os 
import snowflake.connector 
from dotenv import load_dotenv
load_dotenv()
def get_snowflake_connection():
     return snowflake.connector.connect( account="YTEYMEO-FD58545",
                                        authenticator="externalbrowser",
                                        user=os.getenv("SNOWFLAKE_USER"),
                                           warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
                                                  database=os.getenv("SNOWFLAKE_DATABASE"), schema="PUBLIC",)