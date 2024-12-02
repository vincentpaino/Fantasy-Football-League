import mysql.connector
import declarations
import queries
import data

# Define the connection parameters
connection = mysql.connector.connect(
    host="localhost",         # or the server address if hosted remotely
    user="vincentpaino",     # MySQL username
    password="Vin5774593819!", # MySQL password
    database="Fantasy_Football_DB"  
)









#Define connection parameters
def get_connection():
    return mysql.connector.connect(
        host="localhost",         # or the server address if hosted remotely
        user="vincentpaino",      # MySQL username
        password="Vin5774593819!", # MySQL password
        database="Fantasy_Football_DB"
    )

def main():
    connection = get_connection()

    if connection.is_connected():
        print("Connection success!")

    # Creating an instance of 'cursor' class 
    # which is used to execute the SQL 
    # statements in Python
    cursor = connection.cursor()

    cursor.execute(declarations.createDB)

    cursor.execute(queries.query1)

    for x in cursor:
        print(x)

    results = cursor.fetchall()

    for row in results:
        print(row)
    # DECLARATION FUNCTIONS
    # POPULATE FUNCTIONS
    # QUERY FUNCTIONS

    # Ending functions    
    cursor.close()
    connection.close()  

# Ensure this block runs only when the script is executed directly
if __name__ == "__main__":
    main()