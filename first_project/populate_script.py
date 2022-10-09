import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from my_app1.models import AccessRecord, Webpage, Topic, Users
from faker import Faker

fakegen = Faker()

def populate(n=5):

    for entry in range(n):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        persons = Users.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)

if __name__ == '__main__':
    populate(50)
