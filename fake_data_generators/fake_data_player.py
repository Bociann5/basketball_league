import set_up_django_for_generators
set_up_django_for_generators.set_up_django()

import random, time
from league.models import Person, Player

positions = ['point_guard', 'shooting_guard', 'small_forward', 'power_forward', 'center']

def create_players():
    persons = Person.objects.all()
    for person in persons:
        height = random.randrange(155,220)
        weight = random.randrange(70,130)
        age = random.randrange(18,41)
        position = random.choice(positions)
        is_active = random.randrange(0,1)
        player = Player.objects.create(person=person, height=height,
                                        weight=weight, age=age,
                                        position=position, is_active=is_active)
        player.save()

start = time.time()
print('Start', start)
create_players()
print(f'End! It takes {time.time() - start} seconds')