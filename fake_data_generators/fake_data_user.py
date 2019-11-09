import set_up_django_for_generators
set_up_django_for_generators.set_up_django()

import time, random
from faker import Faker
from faker.providers import internet
from django.contrib.auth.models import User

import fake_data_game as game_const


fake = Faker()
fake.add_provider(internet)


def get_username():
    return fake.user_name()

def clear_user_db():
    if User.objects.all().count() > 0:
        User.objects.all().delete()
        print('Cleaned!')

def create_users(nth):
    clear_user_db()

    list_of_users = []
    list_of_username = set()
    for i in range(nth):
        username = get_username()
        if username in list_of_username:
            username = get_username() + str(random.randint(999, 9999))

        list_of_username.add(username)
        password = 'trudne123'
        email = fake.free_email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        u = User(username=username, password=password,
                 email=email, first_name=first_name,
                 last_name=last_name)

        list_of_users.append(u)

    print('Created all list')
    User.objects.bulk_create(list_of_users)

start = time.time()
print('Start', start)
create_users(game_const.NUMBER_OF_ALL_TEAMS * game_const.MAX_NUMBER_PLAYERS_IN_TEAM)
print(f'End! It takes {time.time() - start} seconds')