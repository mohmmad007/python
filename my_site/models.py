from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, reverse


class signin_model(models.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=11)
    users = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')

    def __str__(self):
        return self.users.first_name + ' ' + self.users.last_name


# class suggestion_model(models.Model):
#     name = models.CharField(max_length=20)
#     suggest = models.CharField(max_length=200)
#     users = models.OneToOneField(User, on_delete=models.CASCADE, related_name='suggest_accounts')
    # users = models.ManyToManyField(User, related_name='suggest_fields')
    # id=models.AutoField

    # def __str__(self):
    #     return self.name

class UserProfile(models.Model):
    photo = models.ImageField(upload_to='photos/')