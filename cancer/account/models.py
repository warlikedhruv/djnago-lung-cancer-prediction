from django.db import models
from authentications.models import User
# Create your models here.


class Patient_data(models.Model):
    patient = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    smoking = models.CharField(max_length=10)
    yellow_fingers = models.CharField(max_length=10)
    anxiety = models.CharField(max_length=10)
    peer_pressure = models.CharField(max_length=10)
    chronic_disease = models.CharField(max_length=10)
    fatigue = models.CharField(max_length=10)
    allergy = models.CharField(max_length=10)
    wheezing = models.CharField(max_length=10)
    alcohol = models.CharField(max_length=10)
    coughing = models.CharField(max_length=10)
    short_breath = models.CharField(max_length=10)
    swallowing_difficulty = models.CharField(max_length=10)
    chest_pain = models.CharField(max_length=10)
    image = models.ImageField(upload_to='lungs/', null=True, blank=True)
    prediction = models.CharField(max_length=20, null=True, blank=True)