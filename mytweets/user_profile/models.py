from django.db import models
from django.contrib.auth.models import AbstractBaseUser
class User(AbstractBaseUser):
	"""
	Custom user class.
	"""
	username = models.CharField( 'username', max_length=10,
	unique=True, db_index=True)
	email = models.EmailField('email address', unique=True)
	joined = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'username' #mapped to django username field
	def __unicode__(self):
		return self.username #returns a readable representations of the model object

