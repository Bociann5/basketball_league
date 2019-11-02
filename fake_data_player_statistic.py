import os, django
import random, time

from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basketball_league.settings")
django.setup()
 
from league.models import Player, PlayerStatistic


def create_players_statistic():
    players = Player.objects.all()[:10]
    for player in players:
        points = random.randrange(0,50)
        rebounds = random.randrange(0,25)
        assists = random.randrange(0,25)
        player_statistic = PlayerStatistic.objects.create(player = player, points=points, 
                                            rebounds=rebounds, assists=assists)
        player_statistic.save()
        print(count)

create_players_statistic()