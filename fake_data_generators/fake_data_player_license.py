import set_up_django_for_generators
set_up_django_for_generators.set_up_django()

from league.models import Player, PlayerLicense


def create_players_license():
    uniq_number = 1
    players = Player.objects.all()
    for player in players:
        license_number = uniq_number
        licens = PlayerLicense.objects.create(player=player, license_number=license_number)
        licens.save()
        uniq_number += 1
        print(license_number)

create_players_license()