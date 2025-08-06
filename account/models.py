from django.db import models
from django.contrib.auth.model import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length= 200)
    email = models.CharField(max_length=12)
    phone_number = model.CharField(max_length=12)


    def __str__(self):
        return self.user.username

