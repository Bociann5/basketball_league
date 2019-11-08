import set_up_django_for_generators
set_up_django_for_generators.set_up_django()

import time
from faker import Factory
from league.models import Role, Person

fake = Factory.create()
#
# # TODO change fields in Role Model for BooleanField
def create_roles():
    list_of_roles = []
    IS_ADMIN = True
    IS_MANAGER = True
    IS_PLAYER = True

    for person in Person.objects.all():
        r = Role(is_player=IS_PLAYER, person=person)
        list_of_roles.append(r)

    Role.objects.bulk_create(list_of_roles)

start = time.time()
print('Start', start)
create_roles()
print(f'End! It takes {time.time() - start} seconds')
