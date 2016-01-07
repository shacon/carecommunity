from django.db import models
from profiles.models import Client

class Behavior(models.Model):
    client = models.ManyToManyField(Client)
    description = models.TextField()
    is_positive = models.BooleanField()
    published_date = models.DateTimeField(blank=True, null=True)
    antecedent_text = models.TextField(blank=True, null=True)
    consequence_text = models.TextField(blank=True, null=True)

    def publish(self):
    	self.published_date = time_zone.now()
    	self.save()
        objects = models.Manager()


class Intervention(models.Model):
    behavior = models.ForeignKey(Behavior, null=True, blank=True)
    intervention_text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)

