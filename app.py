import mysql.connector
import declarations.py

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
createLEAGUE = "CREATE TABLE League"
createDRAFT = "CREATE TABLE Draft"
createWEEK = "CREATE TABLE Week"
createOWNER = "CREATE TABLE Owner"
createTEAM = "CREATE TABLE Team"
createROSTER = "CREATE TABLE Roster"
createPLAYER = "CREATE TABLE Player"
createPLAYER_STATS = "CREATE TABLE Player_Stats"
createTRANSACTIONS = "CREATE TABLE Transactions"
createDRAFT_PICKS = "CREATE TABLE Draft_Picks"
createLeague = "CREATE TABLE Point_Rules"

query1 = "SELECT * FROM League"

cursor.execute(createDB)
cursor.execute(query1)
results = cursor.fetchall()

for row in results:
    print(row)




# Ending functions    
cursor.close()
connection.close()  