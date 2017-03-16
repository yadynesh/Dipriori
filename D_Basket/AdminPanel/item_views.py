from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import View
from .models import Item
from django.core.urlresolvers import reverse_lazy

class ItemListView(generic.ListView):
	template_name = "AdminPanel/item_list.html"
	context_object_name = 'item_list'
	def get_queryset(self):
		return Item.objects.all()

class CreateItem(generic.CreateView):
	model = Item
	fields = ['item_name','stocks']
	
class UpdateItem(generic.UpdateView):
	model = Item
	fields = fields = ['item_name','stocks']

class DeleteItem(generic.DeleteView):
	model = Item
	success_url = reverse_lazy('adminpanel:list-items')

# class ItemDetails(generic.DetailView):
# 	model = Item
# 	template_name = "AdminPanel/item-details.html"
