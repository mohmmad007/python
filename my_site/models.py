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
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class UserProfile(models.Model):
    photo = models.ImageField(upload_to='photos/')


# class Document(models.Model):
#     # document_addr = models.FileField(upload_to='documents/')
#     # uploaded_at = models.DateTimeField(auto_now_add=True)
#     document_addr = models.FileField(upload_to='documents/%Y/%m/%d/')
