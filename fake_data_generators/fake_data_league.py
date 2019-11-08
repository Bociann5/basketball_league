import set_up_django_for_generators

set_up_django_for_generators.set_up_django()

import time
from datetime import datetime
from league.models import League, Schedule, Team


def create_league():
    year = datetime.now().year
    league = League.objects.create(season=f'Season of {year} year')
    league.schedule.set([Schedule.objects.get(year=year)])
    league.teams.set(Team.objects.all())
    league.save()

start = time.time()
print('Start', start)
create_league()
print(f'End! It takes {time.time() - start} seconds')