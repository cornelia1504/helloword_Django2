import random

from helloworldapp.models import Person
from faker import Faker
fake = Faker()

#%%
Person.objects.all()
line = Person(name="Annabel Lee", age="33")
line.save()

#%%
for _ in range(10):
  # print(fake.name())
  p = Person(name=fake.name(), age=random.randint(20, 80))
  p.save()

#%%
Person.objects.all()
