import email
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class userData(models.Model):
    fname=models.CharField(max_length=55)
    secordName=models.CharField(max_length=55)
    email_field=models.EmailField(max_length=255)
    phoneNo=models.IntegerField(max_length=255)

    def __str__(self):
        return self.fname


