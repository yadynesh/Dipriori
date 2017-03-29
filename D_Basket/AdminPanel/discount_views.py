from django.views.generic import View
from django.shortcuts import render,redirect
from .models import Item, Discount
from django.conf import settings
from django.views import generic
from django.core.urlresolvers import reverse_lazy


class DiscountListView(generic.ListView):
	template_name = "AdminPanel/discount_list.html"
	context_object_name = 'discount_list'
	def get_queryset(self):
		return Discount.objects.all()

# class CreateDiscount(generic.CreateView):
# 	model = Customer
# 	fields = ['first_name', 'last_name', 'email_id', 'subscribe']
	
class UpdateDiscount(generic.UpdateView):
	model = Discount
	fields = ['left_item1', 'left_item2', 'right_item1', 'right_item2']

class DeleteDiscount(generic.DeleteView):
	model = Discount
	success_url = reverse_lazy('adminpanel:list-discounts')

# class CustomerDiscount(generic.DetailView):
# 	model = Customer
# 	template_name = "AdminPanel/customer-details.html"