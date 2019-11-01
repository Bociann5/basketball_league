
from .set_up_django_for_generators import set_up_django
import time, random
from faker import Factory
from faker.providers import internet
from django.contrib.auth.models import User
from ..league.models import Person

set_up_django()
fake = Factory.create()
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

def create_persons():
    users = User.objects.all()
    for user in users:
        birthday_date = fake.profile(fields=['birthdate'])['birthdate']
        u = User.objects.get(id=user.pk)
        person = Person.objects.create(user=u, first_name=u.first_name,
                                       last_name=u.last_name, birthday_date=birthday_date)
        person.save()

start = time.time()
print('Start', start)
# create_users(100000)
create_persons()
print(f'End! It takes {time.time() - start} seconds')