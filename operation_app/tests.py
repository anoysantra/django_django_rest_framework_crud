# from django.test import TestCase
from models import Cricketers, Batting_Record, Bowling_Record
# Create your tests here.
"""
data = {
    "cricketer": {
        "player_id": "P1031",
        "jersey_no": "189",
        "name": "AMAr Singh",
        "birthdate": "1992-02-11",
        "team": "MI",
        "total_matches_played": 100
    },
    "batting": {
        "runs_scored": 511,
        "innings_played": 115,
        "total_runs": 601,
        "batting_style": "Left-handed"
    },
    "bowling": {
        "innings_bowled": 312,
        "wickets_taken": 501,
        "bowling_style": "Left Arm"
    }
}

print(data['cricketer'])
"""
"""
context = {'player_data': [[{'player_id': 'P001', 'jersey_no': '10', 'name': 'Rocky Singh', 'birthdate': '1990-01-01', 'team': 'RCB', 'total_matches_played': 200}, {'player_id': 'P002', 'jersey_no': '19', 'name': 'AK Das', 'birthdate': '1992-02-11', 'team': 'MI', 'total_matches_played': 110}, {'player_id': 'P003', 'jersey_no': '189', 'name': 'Amar Singh Kaur', 'birthdate': '1992-02-11', 'team': 'MI', 'total_matches_played': 300}, {'player_id': 'P0033', 'jersey_no': '189', 'name': 'AMAr Singh', 'birthdate': '1992-02-11', 'team': 'MI', 'total_matches_played': 100}, {'player_id': 'P0035', 'jersey_no': '189', 'name': 'AMAr Singh', 'birthdate': '1992-02-11', 'team': 'MI', 'total_matches_played': 100}, {'player_id': 'P0036', 'jersey_no': '189', 'name': 'AMAr Singh', 'birthdate': '1992-02-11', 'team': 'MI', 'total_matches_played': 100}, {'player_id': 'P043', 'jersey_no': '81', 'name': 'Santra', 'birthdate': '1992-02-11', 'team': 'SRH', 'total_matches_played': 23}, {'player_id': 'P1031', 'jersey_no': '189', 'name': 'AMAr Singh', 'birthdate': '1992-02-11', 'team': 'MI', 'total_matches_played': 100}, {'player_id': 'P1036', 'jersey_no': '189', 'name': 'AMAr Singh', 'birthdate': '1992-02-11', 'team': 'MI', 'total_matches_played': 100}, {'player_id': 'P1037', 'jersey_no': '189', 'name': 'AMAr Singh', 'birthdate': '1992-02-11', 'team': 'MI', 'total_matches_played': 100}, {'player_id': 'P1038', 'jersey_no': '189', 'name': 'AMAr Singh', 'birthdate': '1992-02-11', 'team': 'MI', 'total_matches_played': 100}, {'player_id': 'P1039', 'jersey_no': '189', 'name': 'AMAr Singh', 'birthdate': '1992-02-11', 'team': 'MI', 'total_matches_played': 100}],
                           [{'player': 'P001', 'innings_played': 150, 'total_runs': 6000, 'batting_style': 'Right-handed'}, {'player': 'P002', 'innings_played': 25, 'total_runs': 585, 'batting_style': 'Left-handed'}, {'player': 'P003', 'innings_played': 115, 'total_runs': 601, 'batting_style': 'Left-handed'}, {'player': 'P0035', 'innings_played': 115, 'total_runs': 601, 'batting_style': 'Left-handed'}, {'player': 'P0036', 'innings_played': 115, 'total_runs': 601, 'batting_style': 'Left-handed'}, {'player': 'P1036', 'innings_played': 115, 'total_runs': 601, 'batting_style': 'Left-handed'}, {'player': 'P1037', 'innings_played': 115, 'total_runs': 601, 'batting_style': 'Left-handed'}, {'player': 'P1038', 'innings_played': 115, 'total_runs': 601, 'batting_style': 'Left-handed'}, {'player': 'P1039', 'innings_played': 115, 'total_runs': 601, 'batting_style': 'Left-handed'}, {'player': 'P1031', 'innings_played': 115, 'total_runs': 601, 'batting_style': 'Left-handed'}, {'player': 'P043', 'innings_played': 20, 'total_runs': 76, 'batting_style': 'Right Handed'}], [{'player': 'P001', 'innings_bowled': 120, 'wickets_taken': 200, 'bowling_style': 'Medium pace'}, {'player': 'P002', 'innings_bowled': 15, 'wickets_taken': 27, 'bowling_style': 'Spinner'}, {'player': 'P003', 'innings_bowled': 312, 'wickets_taken': 500, 'bowling_style': 'Left Arm'}, {'player': 'P0035', 'innings_bowled': 312, 'wickets_taken': 500, 'bowling_style': 'Left Arm'}, {'player': 'P1038', 'innings_bowled': 312, 'wickets_taken': 501, 'bowling_style': 'Left Arm'}, {'player': 'P043', 'innings_bowled': 12, 'wickets_taken': 12, 'bowling_style': 'Left Arm Spinner'}]]}

print(context['player_data'][0])
print(context['player_data'][1])
print(context['player_data'][2])
"""

def get_batting_stats(self):
    return self.batting_record_set.first()
cricketer_instance = Cricketers.objects.get(player_id="example_id")

# Call the get_batting_stats() method
batting_stats = cricketer_instance.get_batting_stats()

# Print the result
print("Batting Stats:", batting_stats)
