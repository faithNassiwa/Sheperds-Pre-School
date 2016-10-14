from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import *

# Create your views here.

def home(request):
	return render(request, 'website/home.html')

def aboutUsLetter(request):
	return render(request, 'website/letter.html')

def mvv(request):
	return render(request, 'website/mvv.html')

def aboutUsTeam(request):
	return render(request, 'website/team.html')

def aboutUsBoard(request):
	return render(request, 'website/board.html')

def facilities(request):
	return render(request, 'website/facilities.html')

def events(request):
	return render(request, 'website/home.html')

def students(request):
	return render(request, 'website/students.html')	

def anthem(request):
	return render(request, 'website/anthem.html')		

def parents(request):
	return render(request, 'website/parents.html')	

def administration(request):
	return render(request, 'website/administration.html')

def fees(request):
	return render(request, 'website/fees.html')

def application(request):
	return render(request, 'website/application.html')			

def careers(request):
	if request.method == 'GET':
		form = CareerForm()
	else:
		form = CareerForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			gender = form.cleaned_data['gender']
			age = form.cleaned_data['age']
			email_address = form.cleaned_data['email_address']
			residential_address = form.cleaned_data['residential_address']
			position_of_interest = form.cleaned_data['position_of_interest']
			motivation = form.cleaned_data['motivation']
			experience = form.cleaned_data['experience']
			work_history = form.cleaned_data['work_history']
			try:
				send_mail(your_name, subject, message, your_email, ['faithnassiwa@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('thanks')

	return render(request, 'website/career.html', {'form': form})							

def contactUs(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			your_name = form.cleaned_data['your_name']
			subject = form.cleaned_data['subject']
			your_email = form.cleaned_data['your_email']
			message = form.cleaned_data['message']
			try:
				send_mail(your_name, subject, message, your_email, ['faithnassiwa@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('thanks')
	return render(request, "website/contact.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your Message. We shall contact you shortly')

def classes(request):
	return render(request, 'website/classes.html')	

def tellyroom(request):
	return render(request, 'website/tellyroom.html')	

def playgrounds(request):
	return render(request, 'website/playgrounds.html')	

def kitchen(request):
	return render(request, 'website/kitchen.html')	

def sickbay(request):
	return render(request, 'website/sickbay.html')	

def washrooms(request):
	return render(request, 'website/washrooms.html')		





