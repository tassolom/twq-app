from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from ..companies.models import Company, Team

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=250, blank=False)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False, blank=False)

    USERNAME_FIELD = "email"

class Employee(User):
    company = models.ForeignKey(Company)
    team = models.ForeignKey(Team, null=True)
