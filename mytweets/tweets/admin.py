from django.contrib import admin
from models import Tweet
# Register your models here.

admin.site.register(Tweet)

def __unicode__(self):
	return self.text
