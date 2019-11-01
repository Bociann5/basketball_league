from .set_up_django_for_generators import set_up_django
from faker import Factory

set_up_django()
fake = Factory.create()