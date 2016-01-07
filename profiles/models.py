from django.db import models
from caretaker.models import Caregiver


class Client(models.Model):
    caregiver = models.ForeignKey(Caregiver)
    nickname = models.CharField(max_length=50)
    #tags = manytomany
	
