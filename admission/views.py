from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.conf import settings
from django.contrib.sessions.models import Session
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView 
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import FormView
#from django.core.mail import send_email
import time 
import datetime
import django
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from .models import *

# Create your views here.
class PreAdmissionCreate(CreateView):
	model = PreAdmission
	fields = ['parent_name', 'phone_number', 'email_address','residential_address', 'child_name', 'child_date_of_birth', 'desired_join_date', 'desired_child_drop_off_time', 'desired_child_pick_up_time']
	template_name = 'admission/application.html'
	#success_url = '/reservations/successful'

	def form_valid(self, form):
		if form.is_valid():	
			form.instance.save()
			return redirect('thanks')

		return super(PreAdmissionCreate, self).form_valid(form)

class CareerCreate(CreateView):
	model = Career
	fields = ['name', 'phone_number', 'email_address','residential_address', 'position_of_interest','desired_join_date','motivation','work_history','academic_qualifications']
	template_name = 'admission/career.html'

	def form_valid(self, form):
		if form.is_valid():	
			form.instance.save()
			return redirect('thanksc')

		return super(CareerCreate, self).form_valid(form)		

def thanks(request):
    return render(request, 'admission/thanks.html')

def thanksc(request):
    return render(request, 'admission/thanksc.html')
