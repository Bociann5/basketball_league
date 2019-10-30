import os, django

from django.contrib.auth.models import User
from league.models import Person
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basketball_league.settings")
django.setup()

fake = Faker()

def create_users(nth):
    for _ in range(nth):
        username = fake.profile(fields=['username'])['username']
        password = 'trudne123'
        email = fake.profile(fields=['mail'])['mail']
        first_name = fake.first_name()
        last_name = fake.last_name()
        User.objects.create_user(username=username, password=password,
                                 email=email, first_name=first_name,
                                 last_name=last_name)

def create_persons():
    max_users_index = User.objects.all().count()
    for ind in range(max_users_index):
        birthday_date = fake.profile(fields=['birthdate'])['birthdate']
        user = User.objects.get(id=max_users_index - ind)
        person = Person.objects.create(user=user, first_name=user.first_name,
                                       last_name=user.last_name, birthday_date=birthday_date)
        person.save()