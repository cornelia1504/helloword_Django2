from django.db import models

# Create your models here.
class Person(models.Model):                    # model - class    - table
    name = models.CharField(max_length=255)  # field - instance - row
    age = models.IntegerField()  # field - instance - row
