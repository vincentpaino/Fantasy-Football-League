#Queries and functions and such

# Determine winning team- This function identifies and outputs the winning 
# team for a specified matchup in a given week, for the user to update the STANDINGS
# table accordingly
query1 = """
SELECT 
    CASE 
        WHEN M.Home_score > M.Away_score THEN M.Home_team_id
        ELSE M.Away_team_id
    END AS Winning_team_id
FROM 
    Matchups AS M
JOIN 
    Week AS W ON M.Week_no = W.Week_no
WHERE 
    W.Current_week = TRUE;
"""

# /This function outputs the player in a specified 
# position who scored the most points in a chosen week.
query2 = """
SELECT P.Fname, P.Lname, P.Player_id
FROM Player AS P
JOIN Player_Stats AS PS
ON P.Player_id = PS.Player_id
WHERE PS.Week_no = 1
  AND PS.Fpts = (
      SELECT MAX(Fpts)
      FROM Player_Stats
      WHERE Week_no = 1
  );
"""

# This function removes a player in a team’s roster
# Specific id must be written in the query 
# Could update TRANSACTIONS
query3p1 = """
DELETE R    
FROM ROSTER AS R
JOIN PLAYER AS P ON R.Player_id = P.Player_id
WHERE R.Player_id = 1000;
"""
query3p2 = """
UPDATE PLAYER
SET Team_id = NULL
WHERE Player_id = 1000;
"""

printPlayer = """
SELECT *
FROM Player
"""