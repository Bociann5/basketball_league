import set_up_django_for_generators

set_up_django_for_generators.set_up_django()

import time
from faker import Faker
from league.models import Team, TeamDetails


fake = Faker()

def create_team_details():
    counter = 1
    for team in Team.objects.all():
        home_color = fake.hex_color()
        away_color = fake.hex_color()

        arena_address = fake.address()
        TeamDetails.objects.create(team=team, home_color=home_color,
                                   away_color=away_color, arena_address=arena_address)
        print(counter)
        counter += 1


start = time.time()
print('Start', start)
create_team_details()
print(f'End! It takes {time.time() - start} seconds')