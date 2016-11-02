from django import forms

class ContactForm(forms.Form):
	your_name = forms.CharField(required = True)
	your_email = forms.EmailField(required=True)
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea)
	

class CareerForm(forms.Form):
	name = forms.CharField(required = True)
	gender = forms.CharField(required = True)
	age = forms.IntegerField(required = True)
	email_address = forms.EmailField(required=True)
	residential_address = forms.CharField(required=True)
	position_of_interest = forms.CharField(required=True)
	motivation = forms.CharField(widget=forms.Textarea)
	experience = forms.CharField(widget=forms.Textarea)	
	work_history = forms.CharField(widget=forms.Textarea)
