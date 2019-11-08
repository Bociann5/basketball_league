import set_up_django_for_generators

set_up_django_for_generators.set_up_django()

import time, pycountry
from faker import Faker
from league.models import Game, Team, Player

list_of_countries = [(country.name, int(country.numeric)) for country in pycountry.countries]
worlds_geo = ['N', 'E', 'W', 'S']
list_teams_names = []
fake = Faker()


# 1
def create_teams():
    counter = 1
    while (Team.objects.all().count() < 330):
        for el in list_of_countries:
            name = ''
            if el[1] % 3 == 0:
                name = f'{fake.last_name()}-{el[0]}-{worlds_geo[0]}'
            elif el[1] % 4 == 0:
                name = f'{fake.last_name()}-{el[0]}-{worlds_geo[1]}'
            elif el[1] % 5 == 0:
                name = f'{fake.last_name()}-{el[0]}-{worlds_geo[2]}'
            else:
                name = f'{fake.last_name()}-{el[0]}-{worlds_geo[3]}'
            Team.objects.create(name=name)
            print('Created! ', counter)
            counter += 1
            if Team.objects.all().count() == 330:
                break



# 2
def add_players_to_teams():
    start_from = 0
    all_players = Player.objects.all().count()

    for team in Team.objects.all():
        print(f'-----TEAM: {team.id}-----')
        players_in_team = []
        for player in Player.objects.all()[start_from::]:
            players_in_team.append(player)
            if len(players_in_team) == 15:
                team.players.set(players_in_team)
                team.save()
                start_from += 15
                players_in_team = []
                break

        if not all_players > start_from:
            break


def create_games():
    all_teams = Team.objects.all().values_list('name', flat=True)
    for team in all_teams:
        for opponent in all_teams:
            if not team == opponent:
                Game.objects.create(host=team, guest=opponent)


start = time.time()
print('Start', start)
# create_teams()
# add_players_to_teams()
create_games()
print(f'End! It takes {time.time() - start} seconds')
