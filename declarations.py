#Table declarations

createDB = """
CREATE DATABASE IF NOT EXISTS Fantasy_Football_DB
"""

createLEAGUE = """
CREATE TABLE IF NOT EXISTS League (
    League_id INT PRIMARY KEY, 
    League_name VARCHAR(50) NOT NULL, 
    No_teams INT, 
    Szn_start DATE, 
    Szn_end DATE, 
    Season_no INT
)
"""

createDRAFT = """
CREATE TABLE IF NOT EXISTS Draft (
    League_id INT PRIMARY KEY, 
    Rounds INT, 
    Pick_order INT, 
    Start_time DATE, 
    End_time DATE, 
    FOREIGN KEY(League_id) REFERENCES League(League_id)
)
"""

createWEEK = """
CREATE TABLE IF NOT EXISTS Week (
    Week_no INT PRIMARY KEY, 
    Current_week BOOLEAN DEFAULT FALSE, 
    Start_date DATE, 
    End_date DATE, 
    League_id INT, 
    FOREIGN KEY(League_id) REFERENCES League(League_id)
)
"""

createOWNER = """
CREATE TABLE IF NOT EXISTS Owner (
    Fname VARCHAR(30), 
    Lname VARCHAR(30), 
    Owner_id INT PRIMARY KEY, 
    League_id INT, 
    FOREIGN KEY(League_id) REFERENCES League(League_id)
)
"""

createTEAM = """
CREATE TABLE IF NOT EXISTS Team (
    Team_id INT PRIMARY KEY, 
    Team_name VARCHAR(30), 
    Owner_id INT, 
    League_id INT, 
    FOREIGN KEY(Owner_id) REFERENCES Owner(Owner_id), 
    FOREIGN KEY(League_id) REFERENCES League(League_id)
)
"""

createSTANDINGS = """
CREATE TABLE IF NOT EXISTS Standings (
    League_id INT, 
    Week_no INT, 
    Team_name VARCHAR(30), 
    Team_rank INT, 
    Wins INT, 
    Losses INT, 
    PRIMARY KEY (League_id, Week_no, Team_name), 
    FOREIGN KEY (League_id) REFERENCES League(League_id)
)
"""

createROSTER = """
CREATE TABLE IF NOT EXISTS Roster (
    Team_id INT, 
    Week_no INT, 
    Player_id INT, 
    Position VARCHAR(2), 
    Lineup_status VARCHAR(20), 
    PRIMARY KEY (Team_id, Player_id, Week_no), 
    FOREIGN KEY(Team_id) REFERENCES Team(Team_id), 
    FOREIGN KEY(Player_id) REFERENCES Player(Player_id), 
    FOREIGN KEY (Week_no) REFERENCES Week(Week_no)
)
"""

createPLAYER = """
CREATE TABLE IF NOT EXISTS Player (
    Fname VARCHAR(30), 
    Lname VARCHAR(30), 
    Player_id INT, 
    Team_id INT, 
    Position VARCHAR(2), 
    Health VARCHAR(25), 
    PRIMARY KEY(Player_id), 
    FOREIGN KEY(Team_id) REFERENCES Team(Team_id)
)
"""

createPLAYER_STATS = """
CREATE TABLE IF NOT EXISTS Player_Stats (
    Player_id INT,
    Week_no INT, 
    Fpts DECIMAL(4,1), 
    Yds INT, 
    Td INT, 
    Recs INT, 
    Fum INT, 
    Xp INT, 
    Fg INT, 
    PRIMARY KEY(Player_id, Week_no), 
    FOREIGN KEY(Player_id) REFERENCES Player(Player_id), 
    FOREIGN KEY(Week_no) REFERENCES Week(Week_no)
)
"""

createTRANSACTIONS = """
CREATE TABLE IF NOT EXISTS Transactions (
    Transaction_id INT PRIMARY KEY, 
    Team_id INT, 
    Player_id INT, 
    Roster_status ENUM('DRAFTED', 'UNDRAFTED') NOT NULL, 
    Date DATE, 
    FOREIGN KEY(Team_id) REFERENCES Team(Team_id), 
    FOREIGN KEY(Player_id) REFERENCES Player(Player_id)
)
"""

createMATCHUPS = """
CREATE TABLE IF NOT EXISTS Matchups (
    Matchup_id INTEGER PRIMARY KEY,
    Week_no INTEGER ,
    Home_team_id INTEGER ,
    Away_team_id INTEGER ,
    Home_score DECIMAL(4, 1),
    Away_score DECIMAL(4, 1),
    FOREIGN KEY (Week_no) REFERENCES Week(Week_no),
    FOREIGN KEY (Home_team_id) REFERENCES Team(Team_id),
    FOREIGN KEY (Away_team_id) REFERENCES Team(Team_id)
)
"""

# createDRAFT_PICKS = """
# CREATE TABLE IF NOT EXISTS Draft_Picks (
#    League_id INT, 
#    Team_id INT, 
#    Player_id INT, 
#    Rank INT, 
#    Pick INT, 
#    Round INT, 
#    PRIMARY KEY(League_id, Pick), 
#    FOREIGN KEY(Team_id) REFERENCES Team(Team_id), 
#    FOREIGN KEY(League_id) REFERENCES League(League_id)
#)
#"""

createPOINT_RULES = """
CREATE TABLE IF NOT EXISTS Point_Rules (
    Pt_type VARCHAR(15) PRIMARY KEY, 
    Pt_value DECIMAL(4,1), 
    Pt_per_yd DECIMAL(4,1)
)
"""


#DECIMAL(4, 1) allows values like 99.9 or 0.1

#Make Current_week attribute a boolean? Yes.






