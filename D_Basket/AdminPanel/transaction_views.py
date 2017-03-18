from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import View
from .models import Customer
from django.core.urlresolvers import reverse_lazy

class TransactionListView(generic.ListView):
	template_name = "AdminPanel/transaction_list.html"
	context_object_name = 'transaction_list'
	def get_queryset(self):
		return Transaction.objects.all()

class CreateTransaction(generic.CreateView):
	model = Transaction
	fields = []
	
class UpdateCustomer(generic.UpdateView):
	model = Transaction
	fields = ['first_name', 'last_name', 'email_id', 'subscribe']

class DeleteCustomer(generic.DeleteView):
	model = Transaction
	success_url = reverse_lazy('adminpanel:list-transactions')

class CustomerDetails(generic.DetailView):
	model = Transaction
	template_name = "AdminPanel/customer-details.html"
