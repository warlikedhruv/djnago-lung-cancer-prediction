from django.db import models

# Create your models here.
acc_type = (('doctor','doctor'), ('patient', 'patient'))
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True, max_length=100)
    password = models.CharField(max_length=20)
    account_type = models.CharField(choices=acc_type, max_length=100)