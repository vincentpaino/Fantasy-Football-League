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

createDB = "CREATE DATABASE FANTASY_FOOTBALL_DB"
createLEAGUE = "CREATE TABLE LEAGUE"
createDRAFT = "CREATE TABLE DRAFT"
createWEEK = "CREATE TABLE WEEK"
createOWNER = "CREATE TABLE OWNER"
createTEAM = "CREATE TABLE TEAM"
createROSTER = "CREATE TABLE ROSTER"
createPLAYER = "CREATE TABLE PLAYER"
createPLAYER_STATS = "CREATE TABLE PLAYER_STATS"
createTRANSACTIONS = "CREATE TABLE TRANSACTIONS"
createDRAFT_PICKS = "CREATE TABLE DRAFT_PICKS"
createLeague = "CREATE TABLE POINT_RULES"
query1 = "SELECT * FROM your_table"

cursor.execute(createDB)
cursor.execute(query1)
results = cursor.fetchall()

for row in results:
    print(row)




# Ending functions    
cursor.close()
connection.close()  