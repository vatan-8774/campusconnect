from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
import datetime
from django.utils import timezone



class User(AbstractUser):
    # Other fields and methods here

    # Add related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='group_permissions',  # Change this to a unique name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions',  # Change this to a unique name
        blank=True,
        help_text='Specific permissions for this user.',
    )
