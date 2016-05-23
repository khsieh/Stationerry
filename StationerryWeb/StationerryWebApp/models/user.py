# This is the file for the User Model

from django.db import models

# Reference: http://www.codeproject.com/Articles/25511/Teach-Yourself-Django-in-Hours-Hour-Creating
# https://docs.djangoproject.com/en/1.9/topics/db/models/

class User(models.Model):
	name = models.CharField('Name'), maxlength=30)
	username = models.CharField('Username', maxlength=26)
	email = models.EmailField('Email', blank=True)
	profilePic = models.ImageField(upload_to='img', blank=True)
	text = models.TextField('Description', maxlength=500, blanky=True)

	def __str__(self):
		return '%s' % (self.name)
		