from django import forms #use to tweek what we want to display on the form
from django.contrib.auth.models import User
from .models import Item,Transaction,Customer
from registration.forms import RegistrationForm
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
		# widgets = {
  #           'cust_id': SearchableSelect(model='AdminPanel.', search_field='name', many=True, limit=10)
  #       }
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


