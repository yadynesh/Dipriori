from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import View
from .models import Customer
from django.core.urlresolvers import reverse_lazy

#generic View used to get the list of customers.
class CustomerListView(generic.ListView):
	template_name = "AdminPanel/customer_list.html"
	context_object_name = 'customer_list'
	def get_queryset(self):
		return Customer.objects.all()
		#retrieving list of Customers which would be stored in context object named 'customer_list' mentioned above.

#generic View used to create a customer.
class CreateCustomer(generic.CreateView):
	model = Customer
	fields = ['first_name', 'last_name', 'email_id', 'subscribe']
	#passing what fields to display on the customer_form
	
#generic View used to update a customer.
class UpdateCustomer(generic.UpdateView):
	model = Customer
	fields = ['first_name', 'last_name', 'email_id', 'subscribe']

#generic View used to delete a customer.
class DeleteCustomer(generic.DeleteView):
	model = Customer
	success_url = reverse_lazy('adminpanel:list-customers')

# class CustomerDetails(generic.DetailView):
# 	model = Customer
# 	template_name = "AdminPanel/customer-details.html"
