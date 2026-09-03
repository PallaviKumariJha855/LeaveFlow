from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)#here we used on_delete to remove all the user related data from the website after deleting his account#CASCADE is used tpo delete the user information from the admin site which is created during makemigrations
    role=models.CharField(max_length=10)#admin or staff

    def __str__(self):
        return self.user.username
