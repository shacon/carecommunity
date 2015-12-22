from django.db import models

class Behavior(models.Model):
    description = models.TextField()
    second_field = models.CharField(max_length=80)
    published_date = models.DateTimeField(
            blank=True, null=True)   

    def publish(self):
	self.published_date = time_zone.now()
	self.save()


    objects = models.Manager()
    

class Intervention(models.Model):   
    intervention_text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)
# Create your models here.
