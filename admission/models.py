from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class PreAdmission(models.Model):
	parent_name = models.CharField(max_length = 100)
	phone_number = models.CharField(max_length = 100)
	email_address = models.CharField(max_length = 100)
	residential_address = models.CharField(max_length = 200)
	child_name = models.CharField(max_length = 100)
	child_date_of_birth = models.DateField(auto_now = False, auto_now_add = False)
	desired_join_date = models.DateField(auto_now = False, auto_now_add = False)
	desired_child_drop_off_time = models.TimeField(auto_now=False, auto_now_add=False)
	desired_child_pick_up_time = models.TimeField(auto_now=False, auto_now_add=False)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

class Career(models.Model):
	name = models.CharField(max_length = 100)
	phone_number = models.CharField(max_length = 100)
	email_address = models.CharField(max_length = 100)
	residential_address = models.CharField(max_length = 200)
	position_of_interest = models.CharField(max_length = 100)
	desired_join_date = models.DateField(auto_now = False, auto_now_add = False)
	motivation = models.TextField()
	work_history = models.TextField()
	academic_qualifications = models.TextField()
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


