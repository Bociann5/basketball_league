import set_up_django_for_generators
set_up_django_for_generators.set_up_django()

import random, time
from league.models import Person, Player

positions = ['point_guard', 'shooting_guard', 'small_forward', 'power_forward', 'center']

def create_players():
    persons = Person.objects.all()
    players_list =[]
    fake_license_number = 1
    for person in persons:
        height = random.randrange(155,220)
        weight = random.randrange(70,130)
        age = random.randrange(18,41)
        position = random.choice(positions)
        is_active = True
        license_number = fake_license_number
        player = Player(
            person=person,
            height=height,
            weight=weight,
            age=age,
            position=position,
            is_active=is_active,
            license_number=license_number
        )
        fake_license_number += 1
        players_list.append(player)
    Player.objects.bulk_create(players_list)

start = time.time()
print('Start', start)
create_players()
print(f'End! It takes {time.time() - start} seconds')