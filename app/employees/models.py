from django.db import models
from account.models import Profile


# Create your models here.


class Position(models.Model):
    position = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.position}-{self.department}'


class Employee(models.Model):
    full_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.full_name}-{self.birth_date}-{self.position}-{self.salary}'
