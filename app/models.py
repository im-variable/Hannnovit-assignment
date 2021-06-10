from django.db import models

from .validator import validate_age
# Create your models here.


class City(models.Model):
    city_name=models.CharField(max_length=200)

    def __str__(self):
        return self.city_name



class Employee(models.Model):
    name = models.CharField(max_length=200)
    pan_number = models.CharField(max_length=200, unique=True, null=False, blank=False)
    age = models.IntegerField(validators=[validate_age])
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def clean(self):
        if self.name:
            self.name =self.name.strip()


