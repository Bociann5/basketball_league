import set_up_django_for_generators
set_up_django_for_generators.set_up_django()

import time, random
import datetime as dt
from faker import Faker
from league.models import Injury, Player, HistoryOfInjury

fake = Faker()

def create_history_of_injuries():
    history_list = []
    for player in Player.objects.all():
        hj = HistoryOfInjury(player=player)
        history_list.append(hj)

    HistoryOfInjury.objects.bulk_create(history_list)

    for history in HistoryOfInjury.objects.all().order_by('id'):
        try:
            inj = Injury.objects.get(id=history.id)
        except Injury.DoesNotExist:
            break
        history.injuries.set([inj])
        history.save()




start = time.time()
print('Start', start)
create_history_of_injuries()
print(f'End! It takes {time.time() - start} seconds')