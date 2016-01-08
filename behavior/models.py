from django.db import models
from profiles.models import Client

class Behavior(models.Model):
    client = models.ForeignKey(Client)
    description = models.TextField()
    is_positive = models.BooleanField()
    published_date = models.DateTimeField(null=True)
    antecedent_text = models.TextField(blank=True)
    consequence_text = models.TextField(blank=True)

    def publish(self):
    	self.published_date = time_zone.now()
    	self.save()
        objects = models.Manager()


class Intervention(models.Model):
    behavior = models.ForeignKey(Behavior)
    intervention_text = models.TextField()
    published_date = models.DateTimeField(
             null=True)

