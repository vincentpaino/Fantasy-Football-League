import mysql.connector

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

createDB = "CREATE DATABASE Fantasy_Football_DB"
query = "SELECT * FROM your_table"
cursor.execute(createDB)
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)




# Ending functions    
cursor.close()
connection.close()