import set_up_django_for_generators

set_up_django_for_generators.set_up_django()

import time, pycountry
from faker import Faker
from league.models import Game, Team, Player

list_of_countries = [(country.name, int(country.numeric)) for country in pycountry.countries]
worlds_geo = ['North', 'East', 'West', 'South']
list_teams_names = []
fake = Faker()

NUMBER_OF_ALL_TEAMS = 230
MAX_NUMBER_PLAYERS_IN_TEAM = 15

# 1
def create_teams():
    counter = 1
    while (Team.objects.all().count() < NUMBER_OF_ALL_TEAMS):
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
            if Team.objects.all().count() == NUMBER_OF_ALL_TEAMS:
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
            if len(players_in_team) == MAX_NUMBER_PLAYERS_IN_TEAM:
                team.players.set(players_in_team)
                team.save()
                start_from += MAX_NUMBER_PLAYERS_IN_TEAM
                players_in_team = []
                break

        if not all_players > start_from:
            break

def create_games():
    all_teams = Team.objects.all().values_list('name', flat=True)
    games_list = []
    for team in all_teams:
        for opponent in all_teams:
            if not team == opponent:
                games_list.append(Game(host=team, guest=opponent))
    Game.objects.bulk_create(games_list)

def assignee_teams_to_games():
    teams_names = Team.objects.all()
    games = Game.objects.all().iterator()
    for game in games:
        game.teams.set(teams_names.filter(name__in=[game.host, game.guest]))


start = time.time()
print('Start', start)
# create_teams()
# add_players_to_teams()
# create_games()
assignee_teams_to_games()
print(f'End! It takes {time.time() - start} seconds')
