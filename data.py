#Populating tables
#DATE data type: YYYY-MM-DD

popLEAGUE = """
INSERT INTO     League(League_id, League_name, No_teams, Szn_start, Szn_end, Season_no)
VALUES          (1, 'CoolLeague2024', 12, '2024-09-05', '2025-01-05', 1),
                (2, 'DemonTimers', 8, '2024-09-05', '2025-01-05', 1)
"""
# Removed Pick_order attribute (refers to league managers)
popDRAFT = """
INSERT INTO     Draft(League_id, Rounds, Start_time, End_time)
VALUES          (1, 15, 2024-08-30, 2024-08-30),
                (2, 15, 2024-08-30, 2024-08-30)
"""
# FIX 
popWEEK = """
INSERT INTO     Week(Week_no, Current_week, Start_date, End_date, League_id)
VALUES          (1, 1, '2024-09-05', '2024-09-12', 1)
"""

popOWNER = """
INSERT INTO     Owner(Fname, Lname, Owner_id, League_id)
VALUES          ('Vince', 'Paino', 100, 1),
                ('Simon', 'Craigery', 101, 1),
                ('Eli', 'Bungus', 102, 2)
"""

popTEAM = """
INSERT INTO     Team(Team_id, Team_name, Owner_id, League_id)
VALUES          (1, 'MontyMyBeloved', 100, 1),
                (2, 'Simon_Craigery', 101, 1),
                (3, 'LetHimCook', 102, 2)
"""

popSTANDINGS = """
INSERT INTO     Standings(League_id, Week_no, Team_name, Team_rank, Wins, Losses)
VALUES          (1, 1, 'MontyMyBeloved', 1, 1, 0),
                (1, 1, 'Simon_Craigery', 2, 0, 1),
                (2, 1, 'LetHimCook', 1, 1, 0)
"""

popROSTER = """
INSERT INTO     Roster(Team_id, Week_no, Player_id, Position, Lineup_status)
VALUES          (1, 1, 1000, 'WR','STARTING'),
                (1, 1, 1001, 'QB','BENCH'),
                (2, 1, 1002, 'RB','STARTING')
"""

popPLAYER = """
INSERT INTO     Player(Fname, Lname, Player_id, Team_id, Position, Health)
VALUES          ('Ceedee', 'Lamb', 1000, 1, 'WR','HEALTHY'),
                ('Patrick', 'Mahomes', 1001, 1, 'QB','QUESTIONABLE'),
                ('Isaiah', 'Pacheco', 1002, 2, 'RB','OUT')
"""

popPLAYER_STATS = """
INSERT INTO     Player_Stats(Player_id, Team_id, Week_no, Fpts, Yds, Td, Recs, Fum, Xp, Fg)
VALUES          (1000, 1, 1, 12.0, 30, 1, 3, 0, 0, 0),
                (1001, 1, 1, 23.0, 200, 1, 0, 0, 0, 0),
                (1002, 1, 1, 16.6, 102, 1, 2, 1, 0, 0)
"""

popTRANSACTIONS = """
INSERT INTO     Transactions(Team_id, Player_id, Roster_status, Date)
VALUES          (1, 1000, 'DRAFTED', '2024-09-05'),
                (1, 1001, 'DRAFTED', '2024-09-05'),
                (2, 1002, 'DRAFTED', '2024-09-05')

"""
# MAKING DRAFT_PICKS OPTIONAL
#popDRAFT_PICKS = """
#INSERT INTO     Draft_Picks(Team_id, Week_no, Player_id, Position, Lineup_status)
#VALUES          (1, 1, 1000, 'WR','HEALTHY'),
#                (1, 1, 1001, 'QB','QUESTIONABLE'),
#                (2, 1, 1002, 'RB','OUT')
#"""

# RETHINK Pt_per_yd ATTRIBUTE
popPOINT_RULES = """
INSERT INTO     Point_Rules(Pt_type, Pt_value, Pt_per_yd)
VALUES          ('TD', 6.0, 6.0),
                ('REC', 1.0, 1.0),
                ('YD', 0.1, 0.1)
"""
