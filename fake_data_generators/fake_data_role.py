from .set_up_django_for_generators import set_up_django
from faker import Factory
from ..league.models import Role, Person

set_up_django()
fake = Factory.create()

# TODO change fields in Role Model for BooleanField
def create_roles():
    list_of_roles = []
    IS_ADMIN = 'True'
    IS_MANAGER = 'True'
    IS_PLAYER = 'True'

    for person in Person.objects.all():
        list_of_roles.append(Role(is_player=IS_PLAYER, person=person))

    Role.objects.bulk_create(list_of_roles)
