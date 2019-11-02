import os, django
import random, time

from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basketball_league.settings")
django.setup()
 
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