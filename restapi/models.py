from django.db import models


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=10)

    # def __str__(self):
    #     return self.name


# Create your models here.
