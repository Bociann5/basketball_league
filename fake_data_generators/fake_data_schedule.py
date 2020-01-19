import set_up_django_for_generators

set_up_django_for_generators.set_up_django()

import time
from datetime import datetime
from league.models import Schedule, Game, Team


def create_schedule():
    year = datetime.now().year
    schedule = Schedule.objects.create(year=year)
    schedule.games.set(Game.objects.all())
    schedule.teams.set(Team.objects.all())
    schedule.save()


start = time.time()
print('Start', start)
create_schedule()
print(f'End! It takes {time.time() - start} seconds')
