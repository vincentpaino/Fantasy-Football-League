import mysql.connector
import declarations

# Define the connection parameters
connection = mysql.connector.connect(
    host="localhost",         # or the server address if hosted remotely
    user="vincentpaino",     # MySQL username
    password="Vin5774593819!", # MySQL password
    database="Fantasy_Football_DB"  
)

if connection.is_connected():
    print("Connection success!")

# Creating an instance of 'cursor' class 
# which is used to execute the 'SQL' 
# statements in 'Python'
cursor = connection.cursor()

query1 = "SELECT * FROM League"

cursor.execute(declarations.createDB)
cursor.execute(query1)
results = cursor.fetchall()

for row in results:
    print(row)




# Ending functions    
cursor.close()
connection.close()  