from faker import Faker
from faker.providers import internet
import time

fake = Faker()

def test():
    counter = 1
    list_username = []
    is_not_same = True
    start = time.time()
    print(time.asctime(time.localtime(start)))
    while is_not_same and len(list_username) < 100000:
        p = fake.profile(fields=['username'])
        list_username.append(p)

        if len(list_username) > 1 and p['username'] in list_username:
            print(f'Fake powtorzyl sie po {counter} razach.')
            is_not_same = False

        counter += 1
    print(f'{(time.time() - start) / 60} seconds.')

fake.add_provider(internet)

print(fake.user_name())