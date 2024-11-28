#Populating tables
#DATE data type: YYYY-MM-DD

popLeague = """
INSERT INTO     League(League_id, League_name, No_teams, Szn_start, Szn_end)
VALUES          (1, 'CoolLeague2024', 12, '2024-09-05', '2025-01-05'),
                (2, 'DemonTime', 8, '2024-09-05', '2025-01-05')
"""
#3NF, fix
popDraft = """
INSERT INTO     Draft(League_id, Rounds, Pick_order, Start_time, End_time)
VALUES          (1, 15, , , ),
                (2, 15, , , , )
"""
#FIX 
popWeek = """
INSERT INTO     Week(Week_no, Current_week, Start_date, End_date, Season, League_id)
VALUES          (1, 1, '2024-09-05', '2024-09-12', 1, 1)
"""

popOwner = """
INSERT INTO     Owner(Fname, Lname, Owner_id, League_id)
VALUES          ('Vince', 'Paino', 100, 1),
                ('Simon', 'Craigery', 101, 1),
                ('Eli', 'Bungus', 102, 2)
"""

popTeam = """
INSERT INTO     Team(Team_id, Team_name, Owner_id, League_id)
VALUES          (1, 'MontyMyBeloved', 100, 1),
                (2, 'Simon_Craigery', 101, 1),
                (3, 'LetHimCook', 102, 2)
"""

popRoster = """
INSERT INTO     Roster(Team_id, Week_no, Player_id, Position, Lineup_status)
VALUES          (1, 1, 1000, 'WR','STARTING'),
                (1, 1, 1001, 'QB','BENCH'),
                (2, 1, 1002, 'RB','STARTING')
"""

popPlayer = """
INSERT INTO     Player(Fname, Lname, Player_id, Team_id, Position, Health)
VALUES          ('Ceedee', 'Lamb', 1000, 'WR','HEALTHY'),
                ('Patrick', 'Mahomes', 1001, 'QB','QUESTIONABLE'),
                ('Isaiah', 'Pacheco', 1002, 'RB','OUT')
"""

popPlayer_Stats = """
INSERT INTO     Player_Stats(Player_id, Team_id, Week_no, Fpts, Yds, Td, Recs, Fum, Xp, Fg)
VALUES          (1000, 1, 1, 12.0, 30, 1, 3, 0, 0, 0),
                (1001, 1, 1, 23.0, 200, 1, 0, 0, 0, 0),
                (1002, 2, 1, 16.6, 102, 1, 2, 1, 0, 0)
"""

popTransactions = """
INSERT INTO     Transactions(Team_id, Player_id, Roster_status, Date)
VALUES          (1, 1000, 'DRAFTED', '2024-09-05'),
                (1, 1001, 'DRAFTED', '2024-09-05'),
                (2, 1002, 'DRAFTED', '2024-09-05'),

"""
#MAKING DRAFT_PICKS OPTIONAL
popDraft_Picks = """
INSERT INTO     Draft_Picks(Team_id, Week_no, Player_id, Position, Lineup_status)
VALUES          (1, 1, 1000, 'WR','HEALTHY'),
                (1, 1, 1001, 'QB','QUESTIONABLE'),
                (2, 1, 1002, 'RB','OUT')
"""
#RETHINK Pt_per_yd ATTRIBUTE
popPoint_Rules = """
INSERT INTO     Point_Rules(Type_id, Pt_type, Pt_value, Pt_per_yd)
VALUES          (1, 'TD', 6.0, 6.0),
                (2, 'REC', 1.0, 1.0),
                (3, 'YD', 0.1, 0.1)
"""
