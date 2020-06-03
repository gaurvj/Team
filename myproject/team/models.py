from django.db import models
from django.urls import reverse


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    logo_url = models.CharField(max_length=500, default=None)
    club_state = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    image_url = models.CharField(max_length=500, default=None)
    player_jersy_number = models.IntegerField(null=False)
    country = models.CharField(max_length=30)



class Match(models.Model):
    team_home = models.ForeignKey(Team, null=True, on_delete=models.CASCADE, related_name='team_home')
    team_away = models.ForeignKey(Team, null=True, on_delete=models.CASCADE, related_name='team_away')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Matches"


class PlayerHistory(models.Model):
    match = models.ForeignKey(Match, null=True, on_delete=models.CASCADE, related_name='match_history')
    team = models.ForeignKey(Team,   null=True, on_delete=models.CASCADE, related_name='team_history')
    player = models.ForeignKey(Player, null=True, on_delete=models.CASCADE, related_name='player_history')
    fifty = models.IntegerField()
    hundred = models.IntegerField()
    high_score = models.IntegerField(default=0)
    total_run = models.IntegerField(default=0)


class Point(models.Model):
    match = models.ForeignKey(Match, null=True, on_delete=models.CASCADE, related_name='match_point')
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE, related_name='team_point')
    point = models.IntegerField()




