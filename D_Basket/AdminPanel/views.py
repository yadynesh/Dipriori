from django.shortcuts import render
from django.views import generic
from .models import Customer

# Create your views here.

class CustomerCreate(generic.CreateView):
	models = Customer
	fields = ['name','email_id','subscribe']
	template_name = "AdminPanel/customer_form.html"
	
	def get_queryset(self):
		return Customer.objects.all()