from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import View
from .models import Item,Transaction
from .forms import TransactionForm
from django.core.urlresolvers import reverse_lazy

class TransactionListView(generic.ListView):
	template_name = "AdminPanel/transaction_list.html"
	context_object_name = 'transaction_list'
	def get_queryset(self):
		return Transaction.objects.all()

class CreateTransaction(View):
	
	def get(self, request, *args, **kwargs):
		the_form = TransactionForm(None)
		context = {
			'form' : the_form
		}
		template_name = "AdminPanel/create_transactions.html"
		return render(request, template_name, context)

	def post(self, request, *args, **kwargs):
		the_form = TransactionForm(request.POST)

		if the_form.is_valid():

			transaction_count = Transaction.objects.count()
			customer = the_form.cleaned_data['cust_id']
			transaction_id = 1
			if transaction_count != 0:
				transaction_id = Transaction.objects.latest('trans_id').trans_id + 1

			item_queryset = the_form.cleaned_data['items']
			for item in item_queryset:
				transaction = Transaction(trans_id = transaction_id,item_id = item,cust_id = customer)
				transaction.save()

		return render(request, "AdminPanel/create_transactions.html",)
	
class UpdateCustomer(generic.UpdateView):
	model = Transaction
	fields = ['first_name', 'last_name', 'email_id', 'subscribe']

class DeleteCustomer(generic.DeleteView):
	model = Transaction
	success_url = reverse_lazy('adminpanel:list-transactions')

class CustomerDetails(generic.DetailView):
	model = Transaction
	template_name = "AdminPanel/customer-details.html"
