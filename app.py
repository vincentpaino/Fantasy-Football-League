import mysql.connector
import declarations
import queries
import data

def get_connection():
    # Connect without specifying the database initially
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vin5774593819!"
    )
    cursor = connection.cursor()
    
    # Create the database if it doesn't exist
    cursor.execute(declarations.createDB)
    cursor.close()

    # Reconnect specifying the database
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vin5774593819!",
        database="Fantasy_Football_DB"
    )

def main():
    connection = get_connection()

    if connection.is_connected():
        print("Connection success!\n")

    # Creating an instance of 'cursor' class 
    # which is used to execute the SQL 
    # statements in Python
    cursor = connection.cursor()

    cursor.execute(declarations.createLEAGUE)
    cursor.execute(declarations.createDRAFT)
    cursor.execute(declarations.createWEEK)
    cursor.execute(declarations.createOWNER)
    cursor.execute(declarations.createTEAM)
    cursor.execute(declarations.createPLAYER)
    cursor.execute(declarations.createSTANDINGS)
    cursor.execute(declarations.createROSTER)
    cursor.execute(declarations.createPLAYER_STATS)
    cursor.execute(declarations.createTRANSACTIONS)
    cursor.execute(declarations.createMATCHUPS)
    # cursor.execute(declarations.createDRAFT_PICKS)
    cursor.execute(declarations.createPOINT_RULES)

    # Clears any loose data from previous tests
    # List of tables to delete (no Draft_Picks table
    
    tables_to_clear = [
        "League", "Draft", "Week", "Owner", "Team", "Roster", "Player",
        "Player_Stats", "Transactions", "Point_Rules"
    ]

    # Delete each table before inserting new data w/o breaking any constraints
    for table in tables_to_clear:
        cursor.execute(f"DELETE FROM {table}")

    cursor.execute(data.popLEAGUE)
    cursor.execute(data.popDRAFT)
    cursor.execute(data.popWEEK)
    cursor.execute(data.popOWNER)
    cursor.execute(data.popTEAM)
    cursor.execute(data.popSTANDINGS)
    cursor.execute(data.popPLAYER)
    cursor.execute(data.popROSTER)
    cursor.execute(data.popPLAYER_STATS)
    cursor.execute(data.popTRANSACTIONS)
    cursor.execute(data.popMATCHUPS)
    # cursor.execute(data.popDRAFT_PICKS)
    cursor.execute(data.popPOINT_RULES)

    # Query executions
    print("The winning teams of the current week are...")
    cursor.execute(queries.query1)

    results = cursor.fetchall()
    for row in results:
        print(row)

    print("\n")
    print("The player with the most Fantasy points in Week 1 was...")
    cursor.execute(queries.query2)

    results = cursor.fetchall()
    for row in results:
        print(row)

    print("Printing Player table...\n")
    cursor.execute(queries.printPlayer)

    results = cursor.fetchall()
    for row in results:
        print(row)

    print("\n")
    print("Removing player from a roster with ID 1000...\n")
    cursor.execute(queries.query3p1)
    cursor.execute(queries.query3p2)
    
    print("Printing updated Player table...\n")
    cursor.execute(queries.printPlayer)

    results = cursor.fetchall()
    for row in results:
        print(row)

    # Ending functions    
    cursor.close()
    connection.close()  

# Ensure this block runs only when the script is executed directly
if __name__ == "__main__":
    main()