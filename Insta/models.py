import random
from django.db import models


def random_integer():
    return random.randint(1000, 9000)


class Contact(models.Model):
    first_name = models.CharField(max_length= 50, default='')
    last_name = models.CharField(max_length= 50, default='')
    number = models.CharField(max_length= 50, default='')
    email = models.CharField(max_length= 50, default='')
    pickup_address = models.CharField(max_length=100, default='')
    plan_options = (('HR', 'Hourly'), ('DY', 'Daily'), ('MN', 'Monthly'), ('EV', 'Event Plan'))
    plan = models.CharField(max_length=1, choices=plan_options, default='HR')
    driver_sex_option = (('MA', 'Male'), ('FE', 'Female'))
    driver_sex = models.CharField(max_length=1, choices=driver_sex_option, default="CC")
    payment_options = (('CS', 'Cash'), ('CC', 'Credit Card'))
    payment = models.CharField(max_length=2, choices=payment_options, default='CC')
    code = models.CharField(default=random_integer(), max_length=4)

    def __str__(self):
        return self.first_name, self.last_name


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    home_address = models.CharField(max_length= 50)
    residence_years = models.CharField(max_length= 50)
    lasdri = models.CharField(max_length= 50)
    experience_years = models.CharField(max_length= 50)

    def __str__(self):
        return self.first_name, self.last_name