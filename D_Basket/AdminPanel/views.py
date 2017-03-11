from django.shortcuts import render
from django.views import generic
from .models import Customer
from django.core.urlresolvers import reverse_lazy

#Create your views here.
#
class IndexView(generic.ListView):
	template_name = "AdminPanel/customer_list.html"
	context_object_name = 'customer_list'
	def get_queryset(self):
		return Customer.objects.all()

class CreateCustomer(generic.CreateView):
	model = Customer
	fields = ['first_name', 'last_name', 'email_id', 'subscribe']
	
class UpdateCustomer(generic.UpdateView):
	model = Customer
	fields = ['first_name', 'last_name', 'email_id', 'subscribe']

class DeleteCustomer(generic.DeleteView):
	model = Customer
	success_url = reverse_lazy('adminpanel:list-customers')

class CustomerDetails(generic.DetailView):
	model = Customer
	template_name = "AdminPanel/customer-details.html"