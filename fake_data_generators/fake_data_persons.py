import set_up_django_for_generators
set_up_django_for_generators.set_up_django()

import time
from faker import Faker
from django.contrib.auth.models import User
from league.models import Person

fake = Faker()

def create_persons():
    users = User.objects.all()
    for user in users:
        birthday_date = fake.profile(fields=['birthdate'])['birthdate']
        u = User.objects.get(id=user.pk)
        Person.objects.create(user=user, first_name=user.first_name,
                                       last_name=user.last_name, birthday_date=birthday_date)

start = time.time()
print('Start', start)
create_persons()
print(f'End! It takes {time.time() - start} seconds')