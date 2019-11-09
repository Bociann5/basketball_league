import set_up_django_for_generators
set_up_django_for_generators.set_up_django()

import random, time
from league.models import Player, PlayerStatistic


def create_players_statistic():
    players = Player.objects.all()
    stats_list = []
    for player in players:
        points = random.randrange(0,50)
        rebounds = random.randrange(0,25)
        assists = random.randrange(0,25)
        ps = PlayerStatistic(player = player, points=points,
                                            rebounds=rebounds, assists=assists)
        stats_list.append(ps)
    PlayerStatistic.objects.bulk_create(stats_list)


start = time.time()
print('Start', start)
create_players_statistic()
print(f'End! It takes {time.time() - start} seconds')