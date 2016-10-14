from django.contrib import admin
from django.contrib.admin import sites
from .models import *
from django.contrib.admin.sites import AdminSite
from django.utils.translation import ugettext_lazy

class PreAdmissionAdmin(admin.ModelAdmin):
	list_display= ('parent_name', 'phone_number', 'email_address','residential_address', 'child_name', 'child_date_of_birth', 'desired_join_date', 'desired_child_drop_off_time', 'desired_child_pick_up_time', 'created_at', 'updated_at')
	list_filter = ('created_at', 'updated_at')
	search_fields = ['parent_name']

class CareerAdmin(admin.ModelAdmin):
	list_display= ('name', 'phone_number', 'email_address','residential_address', 'position_of_interest','desired_join_date','motivation','work_history','academic_qualifications', 'created_at', 'updated_at')
	list_filter = ('created_at', 'updated_at')
	search_fields = ['name']
	
# Register your models here.
admin.site.register(PreAdmission, PreAdmissionAdmin)
admin.site.register(Career, CareerAdmin)