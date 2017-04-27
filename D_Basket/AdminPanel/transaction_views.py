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


#generic View to retieve list of transactions
class TransactionListView(generic.ListView):
	template_name = "AdminPanel/transaction_list.html"
	context_object_name = 'transaction_list'
	def get_queryset(self):
		return Transaction.objects.all()

#This class is used to create a Transaction.
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
				#getting the latest transaction number. transaction_id =  latest-transaction-number + 1 
				transaction_id = Transaction.objects.latest('trans_id').trans_id + 1

			item_queryset = the_form.cleaned_data['items']
			print(type(item_queryset))

			retrieved_item_id_list = []
			for item in item_queryset:
				#Adding a new transaction entry for every item bought by the customer.
				transaction = Transaction(trans_id = transaction_id,item_id = item,cust_id = customer)

				#adding id of every item bought by customer to the retrieved_item_id_list
				retrieved_item_id_list.append(item.id)
				transaction.save()

			
			all_items = Item.objects.all()
			all_item_id_list = []

			for item in all_items:
				'''
				Scanning through list of all items in the database and adding 1 to all_item_id_list 
				if that item was bought by the customer else 0
				'''
				if item.id not in retrieved_item_id_list:
					all_item_id_list.append(0)
				else:
					all_item_id_list.append(1)

			print(all_item_id_list)

			with open(settings.BASE_DIR+"/AdminPanel/Final_Original2.csv", 'a',newline='') as csvfile:
			    spamwriter = csv.writer(csvfile,
			                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
			    spamwriter.writerow(all_item_id_list)


			return redirect('adminpanel:list-transactions')

			
		return reverse(request, "AdminPanel/transaction_form.html",)


#generic View to update a transaction	
class UpdateTransaction(generic.UpdateView):
	model = Transaction
	fields = ['cust_id','item_id']

#generic View to delete a transaction
class DeleteTransaction(generic.DeleteView):
	model = Transaction
	success_url = reverse_lazy('adminpanel:list-transactions')


