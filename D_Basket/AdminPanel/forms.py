from django import forms #use to tweek what we want to display on the form
from django.contrib.auth.models import User
from .models import Item, Transaction, Customer, Configuration
from registration.forms import RegistrationForm
from django.core.validators import validate_ipv4_address
# from searchableselect.widgets import SearchableSelect

class TransactionForm(forms.ModelForm):
	items = forms.ModelMultipleChoiceField(queryset = Item.objects.all(),
			widget = forms.CheckboxSelectMultiple(
				attrs = {
					"class": "btn btn-primary"
				}
			)
		)

	class Meta:
		model = Transaction
		fields = ['cust_id']
		


class ConfigurationForm(forms.Form):
		email_id = forms.EmailField(
			label = "Email Id",
			widget = forms.EmailInput(
				attrs = {
					"placeholder" : "eg: abc@gmail.com",
					"class" : "form-control"
				}
			)
		)
		email_password = forms.CharField(
			label = "Password",
			widget = forms.PasswordInput(
				attrs = {
					"placeholder" : "Enter Password",
					"class" : "form-control"
				}
			)
		)
		server_ip_address = forms.CharField(
			label = "Server Ip Address",
			validators = [validate_ipv4_address],
			widget = forms.TextInput(
				attrs = {
					"placeholder" : "eg.127.0.0.1",
					"class" : "form-control"
				}
			)
		)
		local_minimum_support = forms.CharField(
			label = "Local Minimum Support Percentage",
			widget = forms.NumberInput(
				attrs = {
					"placeholder" : "1-100",
					"class" : "form-control",
					"min" : "1",
					"max" : "100",
				}
			)
		)
		local_confidence = forms.CharField(
			label = "Confidence Percentage",
			widget = forms.NumberInput(
				attrs = {
					"placeholder" : "1-100",
					"class" : "form-control",
					"min" : "1",
					"max" : "100",
				}
			)
		)
		

						
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
