from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"


class Passenger(models.Model):
    # Your existing fields
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    age = models.IntegerField()
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
        ('Prefer not to say', 'Prefer not to say'),
    ]
    gender = models.CharField(max_length=20, choices=gender_choices)
    citizenship = CountryField()
    passport_id = models.CharField(max_length=8, unique=True, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old."
