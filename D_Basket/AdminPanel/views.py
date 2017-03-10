from django.shortcuts import render
from django.views import generic
from .models import Customer
from django.core.urlresolvers import reverse_lazy

# Create your views here.
# class IndexView(generic.ListView):
# 	template_name = "AdminPanel/index.html"
# 	context_object_name = 'all_customers'
# 	def get_queryset(self):
# 		return Customer.objects.all()

class CreateCustomer(generic.CreateView):
	model = Customer
	fields = ['name','email_id','subscribe']
	
class UpdateCustomer(generic.UpdateView):
	model = Customer
	fields = ['name','email_id','subscribe']

class DeleteCustomer(generic.DeleteView):
	model = Customer
	success_url = reverse_lazy('adminpanel:add-customer')

class CustomerDetails(generic.DetailView):
	model = Customer
	template_name = "AdminPanel/customer-details.html"