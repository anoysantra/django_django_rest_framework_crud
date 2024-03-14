from django.db import models

# Create your models here.


class Cricketers(models.Model):
    player_id = models.CharField(max_length=5, primary_key=True)
    jersey_no = models.CharField(max_length=4)
    name = models.CharField(max_length=100, null=False)
    birthdate = models.DateField()
    team = models.CharField(max_length=50, null=False)
    total_matches_played = models.PositiveIntegerField()

    """
    def get_batting_stats(self):
        return self.batting_record_set.first()

    def get_bowling_stats(self):
        return self.bowling_record_set.first()
    """


class Batting_Record(models.Model):
    player = models.ForeignKey(Cricketers, on_delete=models.CASCADE)
    innings_played = models.PositiveIntegerField()
    total_runs = models.PositiveIntegerField()
    batting_style = models.CharField(max_length=50)


class Bowling_Record(models.Model):
    player = models.ForeignKey(Cricketers, on_delete=models.CASCADE)
    innings_bowled = models.PositiveIntegerField()
    wickets_taken = models.PositiveIntegerField()
    bowling_style = models.CharField(max_length=100)
