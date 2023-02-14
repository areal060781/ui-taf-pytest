from faker import Faker
'''https://faker.readthedocs.io/en/master/index.html#'''
fake = Faker('es_MX')

print(fake.first_name())
print(fake.last_name())
print(fake.email())
# 'Lucy Cechtelar'

print(fake.address())
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

print(fake.phone_number())

print(f'Random int: {fake.random_int()}')
print(f'Random int: {fake.random_int(500, 99999)}')
