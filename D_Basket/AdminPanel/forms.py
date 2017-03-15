from .models import Admin #importing the base user class

from django import forms #use to tweek what we want to display on the form

from registration.forms import RegistrationForm

class AdminForm(RegistrationForm):
	username = forms.CharField(
			label = "Username",
			widget = forms.TextInput(
				attrs = {
					"placeholder" : "Enter username",
					"class" : "form-control"
				}
			)
		)

	email = forms.EmailField(
			label = "Email Id",
			widget = forms.EmailInput(
				attrs = {
					"placeholder" : "eg: abc@gmail.com",
					"class" : "form-control"
				}
			)
		)

	password1 = forms.CharField(
			label = "Password",
			widget = forms.PasswordInput(
				attrs = {
					"placeholder" : "Enter Password",
					"class" : "form-control"
				}
			)
		)

	password2 = forms.CharField(
			label = "Re-enter password",
			widget = forms.PasswordInput(
				attrs = {
					"placeholder" : "Re-enter password",
					"class" : "form-control"
				}
			)
		)

