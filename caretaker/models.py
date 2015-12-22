from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CaregiverManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name):
	email = self.normalize_email(email)
	user = self.model(email=email, first_name=first_name, last_name=last_name, is_staff=False, is_active=True)
	user.set_password(password)
	user.save()
  
class Caregiver(AbstractBaseUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = CaregiverManager()

    def get_full_name(self):
	return self.first_name + ' ' + self.last_name
    
    def get_short_name(self):
	return self.first_name


class Profile(models.Model):
    caregiver = models.ForeignKey(Caregiver)
    problem_behaviors = models.TextField()
    strengths = models.TextField()
    



# Create your models here.
