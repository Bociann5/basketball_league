from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    winner = models.CharField(max_length=150, blank=True, null=True)
    loser = models.CharField(max_length=150, blank=True, null=True)
    guest = models.ForeignKey('Team', related_name='game_guest', on_delete=models.CASCADE)
    host = models.ForeignKey('Team', related_name='game_host', on_delete=models.CASCADE)
    date_match = models.CharField(max_length=100, blank=True, null=True)
    score_guest = models.CharField(max_length=10, blank=True, null=True)
    score_host = models.CharField(max_length=10, blank=True, null=True)
    final_score = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.host} - {self.guest}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Schedule(models.Model):
    year = models.CharField(max_length=30, blank=True, null=True)
    games = models.ManyToManyField(Game, related_name='schedules')


class Person(models.Model):
    user = models.ForeignKey(User, related_name='persons', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    birthday_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.last_name


class Role(models.Model):
    is_admin = models.BooleanField(blank=True, null=True)
    is_manager = models.BooleanField(blank=True, null=True)
    is_player = models.BooleanField(blank=True, null=True)
    person = models.ForeignKey(Person, related_name='roles', on_delete=models.CASCADE)

class Player(models.Model):
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.BooleanField(null=True)
    person = models.ForeignKey(Person, related_name='players', on_delete=models.CASCADE)
    license_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.person.last_name


class PlayerStatistic(models.Model):
    player = models.ForeignKey(Player, related_name='player_statistics', on_delete=models.CASCADE)
    points = models.IntegerField(blank=True, null=True)
    rebounds = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.player.person.last_name


class Team(models.Model):
    players = models.ManyToManyField(Player, related_name='teams')
    games = models.ManyToManyField(Game, related_name='teams')
    name = models.CharField(max_length=150, blank=True, null=True)
    amount_of_wins = models.IntegerField(blank=True, null=True)
    amount_of_losses = models.IntegerField(blank=True, null=True)
    records = models.CharField(max_length=45, blank=True, null=True)
    founding_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class TeamDetails(models.Model):
    home_color = models.CharField(max_length=45, blank=True, null=True)
    away_color = models.CharField(max_length=45, blank=True, null=True)
    arena_address = models.CharField(max_length=225, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_details')


class League(models.Model):
    season = models.CharField(max_length=45, blank=True, null=True)
    schedule = models.ManyToManyField(Schedule, related_name='leagues')
    teams = models.ManyToManyField(Team, related_name='leagues')


class Injury(models.Model):
    date_of_accident = models.DateField(blank=True, null=True)
    break_time = models.IntegerField(blank=True, null=True)
    type_of_injury = models.CharField(max_length=45, blank=True, null=True)


class HistoryOfInjury(models.Model):
    player = models.ForeignKey(Player, related_name='histories_of_injuries', on_delete=models.CASCADE)
    injuries = models.ManyToManyField(Injury, related_name='histories_of_injuries')