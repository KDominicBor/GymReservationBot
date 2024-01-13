# reservation_app/models.py

from django.db import models

class Reservation(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # Add more fields as needed
