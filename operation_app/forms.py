from django import forms
from .models import Batting_Record, Bowling_Record, Cricketers

"""
class CricketersForm(forms.ModelForm):
    class Meta:
        model = Cricketers
        field_name = ['player_id', 'jersey_no', 'name',
                      'birthdate', 'team', 'total_matches_played']


class BattingForm(forms.ModelForm):
    class Meta:
        model = Bowling_Record
        field_name = ['innings_played',
                      'total_runs', 'batting_style']


class BowlingForm(forms.ModelForm):
    class Meta:
        model = Batting_Record
        field_name = ['innings_bowled',
                      'wickets_taken', 'bowling_style']
"""


class CombinedDataForm(forms.Form):
    player_id = forms.CharField(max_length=5)
    jersey_no = forms.CharField(max_length=4)
    name = forms.CharField(max_length=100)
    birthdate = forms.DateField()
    team = forms.CharField(max_length=50)
    total_matches_played = forms.IntegerField()
    innings_played = forms.IntegerField()
    total_runs = forms.IntegerField()
    batting_style = forms.CharField(max_length=50)
    innings_bowled = forms.IntegerField()
    wickets_taken = forms.IntegerField()
    bowling_style = forms.CharField(max_length=100)
