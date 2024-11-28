#Populating tables
#DATE data type: YYYY-MM-DD

popLeague = """
INSERT INTO     League(League_id, League_name, No_teams, Szn_start, Szn_end)
VALUES          (1, CoolLeague2024, 12, 2024-09-05, 2025-01-05),
                (2, DemonTime, 8, 2024-09-05, 2025-01-05)
"""

popDraft = """
INSERT INTO     Draft(League_id, Rounds, Pick_order, Start_time, End_time)
VALUES          (1, 15, , , ),
                (2, 15, , , , )
"""

popWeek = """
INSERT INTO     League(League_id, League_name, No_teams, Szn_start, Szn_end)
VALUES          (1, CoolLeague2024, 12, 2024-09-05, 2025-01-05),
                (2, DemonTime, 8, 2024-09-05, 2025-01-05)
"""

popOwner = """

"""

popTeam = """

"""

popRoster = """

"""

popPlayer = """

"""

popPlayer_stats = """

"""

popTransactions = """

"""

popDraft_picks = """

"""

popPoint_rules = """

"""
