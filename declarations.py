#Table declarations
createDB = "CREATE DATABASE Fantasy_Football_DB"
createLEAGUE = "CREATE TABLE League(League_id INT AUTO_INCREMENT PRIMARY KEY, League_name VARCHAR(50) NOT NULL, No_teams INT, Szn_start DATE, Szn_end DATE)"
createDRAFT = "CREATE TABLE Draft(League_id INT, Rounds INT, Pick_order INT, Start_time DATE, End_time DATE, FOREIGN KEY(League_id) REFERENCES League(League_id) )"
createWEEK = "CREATE TABLE Week(Week_no INT, Current_week INT, Start_date DATE, End_date DATE, Season INT, League_id INT, UNIQUE(Week_no), PRIMARY KEY(Week_no), FOREIGN KEY(League_id) REFERENCES League(League_id) )"
createOWNER = "CREATE TABLE Owner(Fname VARCHAR(30), Lname VARCHAR(30), Owner_id INT, League_id INT, UNIQUE(Owner_id), PRIMARY KEY(Owner_id), FOREIGN KEY(League_id) REFERENCES League(League_id) )"
createTEAM = "CREATE TABLE Team(Team_id INT, Team_name VARCHAR(30), Owner_id INT, League_id INT,UNIQUE(Team_id) PRIMARY KEY(Team_id), FOREIGN KEY(Owner_id), FOREIGN KEY(League_id) REFERENCES League(League_id) )"
createROSTER = "CREATE TABLE Roster(Team_id INT, Week_no INT, Player_id INT, Position VARCHAR(2), Lineup_status VARCHAR(20), FOREIGN KEY(Team_id)  )"
createPLAYER = "CREATE TABLE Player(Fname VARCHAR(30),Lname VARCHAR(30), Player_id INT, Team_id INT, Position VARCHAR(2), Health VARCHAR(25), PRIMARY KEY(Player_id), FOREIGN KEY(Team_id) REFERENCES Team(Team_id))"
createPLAYER_STATS = "CREATE TABLE Player_Stats(Player_id INT, Team_id INT, Week_no INT, Fpts DECIMAL(4,1), Yds INT, Td INT, Recs INT, Fum INT, Xp INT, Fg INT, FOREIGN KEY(Player_id) REFERENCES Player(Player_id))"
createTRANSACTIONS = "CREATE TABLE Transactions(Team_id INT, Player_id INT, Roster_status VARCHAR(15), Date DATE, FOREIGN KEY(Team_id) REFERENCES Team(Team_id), FOREIGN KEY(Player_id) REFERENCES Player(Player_id))"
createDRAFT_PICKS = "CREATE TABLE Draft_Picks(League_id INT, Team_id INT, Player_id INT, Rank INT, Pick INT, Round INT, PRIMARY KEY(Pick), FOREIGN KEY(Team_id) REFERENCES Team(Team_id), FOREIGN KEY(League_id) REFERENCES League(League_id)) "
createPOINT_RULES = "CREATE TABLE Point_Rules(Type_id INT, Pt_type VARCHAR(15), Pt_value DECIMAL(4,1), Pt_per_yd DECIMAL(4, 1), PRIMARY KEY(Type_id))"
#DECIMAL(4, 1) allows values like 99.9 or 0.1

#Make Current_week attribute a boolean?






