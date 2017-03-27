from django.conf import settings
from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import View
from .models import Item,Transaction
from .forms import TransactionForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
import pandas
import csv

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
		template_name = "AdminPanel/transaction_form.html"
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
			print(type(item_queryset))

			retrieved_item_id_list = []
			for item in item_queryset:
				transaction = Transaction(trans_id = transaction_id,item_id = item,cust_id = customer)
				retrieved_item_id_list.append(item.id)
				transaction.save()

			
			all_items = Item.objects.all()
			all_item_id_list = []

			for item in all_items:
				if item.id not in retrieved_item_id_list:
					all_item_id_list.append(0)
				else:
					all_item_id_list.append(1)

			print(all_item_id_list)

			with open(settings.BASE_DIR+"/AdminPanel/Final_Original1.csv", 'a',newline='') as csvfile:
			    spamwriter = csv.writer(csvfile,
			                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
			    spamwriter.writerow(all_item_id_list)


			return redirect('adminpanel:list-transactions')

			
		return reverse(request, "AdminPanel/transaction_form.html",)
	
class UpdateTransaction(generic.UpdateView):
	model = Transaction
	fields = ['cust_id','item_id']

class DeleteTransaction(generic.DeleteView):
	model = Transaction
	success_url = reverse_lazy('adminpanel:list-transactions')

class CustomerDetails(generic.DetailView):
	model = Transaction
	template_name = "AdminPanel/customer-details.html"
