import set_up_django_for_generators
set_up_django_for_generators.set_up_django()

import random
from league.models import Player, PlayerStatistic


def create_players_statistic():
    players = Player.objects.all()
    count = 1
    for player in players:
        points = random.randrange(0,50)
        rebounds = random.randrange(0,25)
        assists = random.randrange(0,25)
        PlayerStatistic.objects.create(player = player, points=points,
                                            rebounds=rebounds, assists=assists)
        print(count)
        count += 1

create_players_statistic()