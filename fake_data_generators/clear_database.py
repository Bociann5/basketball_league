import set_up_django_for_generators

set_up_django_for_generators.set_up_django()

from league.models import (
    User,
    Game,
    Team,
    TeamDetails,
    Schedule,
    League,
    HistoryOfInjury,
    Injury
)

def clear_database():
    User.objects.all().delete()
    print('Users Deleted')
    Game.objects.all().delete()
    print('Games Deleted')
    Team.objects.all().delete()
    print('Teams Deleted')
    TeamDetails.objects.all().delete()
    print('Team Details Deleted')
    Schedule.objects.all().delete()
    print('Schedule Deleted')
    League.objects.all().delete()
    print('League Deleted')
    HistoryOfInjury.objects.all().delete()
    print('History Deleted')
    Injury.objects.all()
    print('Injury Deleted')


clear_database()
