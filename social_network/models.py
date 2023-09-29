from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
import datetime
from django.utils import timezone


class User(AbstractUser):
    # Other fields and methods here

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_specific_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    department = models.CharField(max_length=50, blank=True)
    year_of_study = models.CharField(max_length=10, null=True, blank=True)

    

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_gender(self):
        return self.gender
    
    def get_department(self):
        return self.department
    
    def get_year_of_study(self):
        return self.year