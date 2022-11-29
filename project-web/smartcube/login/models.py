from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11, default='13488508087')

    def __str__(self):
        return self.first_name + self.last_name + ':' + self.phone_number
