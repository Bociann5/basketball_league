import set_up_django_for_generators
set_up_django_for_generators.set_up_django()

import time, random
import datetime as dt
from faker import Faker
from league.models import Injury
# import fake_data_game as game_const

# NUMBER_OF_ALL_PLAYERS = game_const.NUMBER_OF_ALL_TEAMS * game_const.MAX_NUMBER_PLAYERS_IN_TEAM
PERCENTAGE_OF_INJURIES = random.random()
fake = Faker()
TYPE_OF_INJURIES = ['Sprains', 'Strains',
                    'Knee injuries','Swollen muscles',
                    'Achilles tendon rupture', 'Fractures'
                    'Dislocations', 'Rotator cuff injury']

def create_injuries():
    date_of_accident = dt.datetime.now().date()
    for inj in range(int(PERCENTAGE_OF_INJURIES * 230 * 15)):
        go_back_in_days = random.randrange(1, 200)
        date_of_accident = date_of_accident - dt.timedelta(days=go_back_in_days)
        break_time = random.randrange(1, 49)
        type_of_injuries = random.randrange(0, len(TYPE_OF_INJURIES))
        Injury.objects.create(break_time=break_time,
                              date_of_accident=date_of_accident,
                              type_of_injury=TYPE_OF_INJURIES[type_of_injuries])
        print('Created ', inj)


create_injuries()