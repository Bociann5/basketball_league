import set_up_django_for_generators
set_up_django_for_generators.set_up_django()

import time
from league.models import Player, PlayerLicense


def create_players_license():
    uniq_number = 1
    license_list = []
    players = Player.objects.all()
    for player in players:
        license_number = uniq_number
        licens = PlayerLicense(player=player, license_number=license_number)
        license_list.append(licens)
        uniq_number += 1

    PlayerLicense.objects.bulk_create(license_list)


start = time.time()
print('Start', start)
create_players_license()
print(f'End! It takes {time.time() - start} seconds')
