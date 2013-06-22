from django.db import models
from django.utils import timezone
import datetime

# Create your models here

class Vendor(models.Model):
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date_published')
    
    def __unicode__(self):
		return self.name
	
    def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		was_published_recently.admin_order_field = 'pub_date'
		was_published_recently.boolean = True
		was_published_recently.short_description = 'Published recently'
 
class VendorDetails(models.Model):
	vendor = models.ForeignKey(Vendor)
	description = models.CharField(max_length=1000)
	internalPOV = models.CharField(max_length=1000)
    externalPOV = models.charField(max_length=1000)
	def __unicode__(self):
		return self.description

class VendorVisits(models.Model):
    vendor = models.ForeignKey(Vendor)
    meetingDate = models.DateTimeField('meeting_date')
    

