from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    winner = models.CharField(max_length=45, blank=True, null=True)
    loser = models.CharField(max_length=45, blank=True, null=True)
    guest = models.CharField(max_length=45, blank=True, null=True)
    host = models.CharField(max_length=45, blank=True, null=True)
    date_match = models.CharField(max_length=45, blank=True, null=True)
    score_guest = models.CharField(max_length=45, blank=True, null=True)
    score_host = models.CharField(max_length=45, blank=True, null=True)
    final_score = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return f'{self.guest} - {self.host}'

class Person(models.Model):
    user = models.ForeignKey(User, related_name='persons', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    birthday_date = models.DateField(blank=True, null=True)  

    def __str__(self):
        return self.last_name 

class Player(models.Model):
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    person = models.ForeignKey(Person, related_name='players', on_delete=models.CASCADE)

    def __str__(self):
        return self.person