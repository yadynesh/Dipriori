from django.contrib.auth.models import User #importing the base user class

from django import forms #use to tweek what we want to display on the form

class AdminForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']