#Queries and functions and such

# Determine winning team This function identifies and outputs the winning 
# team for a specified matchup in a given week, and updates the standings accordingly
query1 = """
SELECT * 
FROM League
WHERE No_teams > 12
"""

# /This function outputs the player in a specified 
# position who scored the most points in a given week.
query2 = """
SELECT * 
FROM League
WHERE No_teams > 12
"""

# This function removes a player in a team’s roster
query3 = """
UPDATE   
FROM League
WHERE No_teams > 12
"""