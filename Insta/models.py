from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    number = models.CharField(max_length= 50)
    email = models.CharField(max_length= 50)
    pickup_address = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.first_name, self.last_name


class Plan(models.Model):
    plan_options = (('HR', 'Hourly'),('DY', 'Daily'),('MN', 'Monthly'),('EV', 'Event Plan'))
    plan = models.CharField(max_length= 1, choices=plan_options, default="Event Plan")
    driver_sex_option = (('MA', 'Male'), ('FE', 'Female'))
    driver_sex = models.CharField(max_length= 1, choices=driver_sex_option, default="Male")
    payment_options = (('CS', 'Cash'), ('CC', 'Credit Card'))
    payment = models.CharField(max_length=1, choices=payment_options)

    def __str__(self):
        return self.plan, self.payment


class Driver(models.Model):
    number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    home_address = models.CharField(max_length= 50)
    residence_years = models.CharField(max_length= 50)
    lasdri = models.CharField(max_length= 50)
    driver_sex_option = (('MA', 'Male'), ('FE', 'Female'))
    driver_sex = models.CharField(max_length= 1, choices=driver_sex_option, default="Male")
    experience_years = models.CharField(max_length= 50)

    def __str__(self):
        return self.first_name, self.last_name