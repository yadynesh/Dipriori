from django.views.generic import View
from django.shortcuts import render,redirect
from .models import Item, Discount, Customer
from django.conf import settings
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail


class DiscountListView(generic.ListView):
	template_name = "AdminPanel/discount_list.html"
	context_object_name = 'discount_list'
	def get_queryset(self):
		return Discount.objects.all()

class UpdateDiscount(generic.UpdateView):
	model = Discount
	fields = ['left_item1', 'left_item2', 'right_item1', 'right_item2']

class DeleteDiscount(generic.DeleteView):
	model = Discount
	success_url = reverse_lazy('adminpanel:list-discounts')


# class CreateDiscount(generic.CreateView):
# 	model = Customer
# 	fields = ['first_name', 'last_name', 'email_id', 'subscribe']


# class CustomerDiscount(generic.DetailView):
# 	model = Customer
# 	template_name = "AdminPanel/customer-details.html"

def sendDiscountMail(request):

	discount_left = request.POST['discount_left']
	discount_right = request.POST['discount_right']
	print(discount_right)
	message = "Buy " + discount_left + " and get " + discount_right + " free."
	subscribed_customers = Customer.objects.filter(subscribe=True)
	subscribed_customers_email = []

	for customer in subscribed_customers:
		subscribed_customers_email.append(customer.email_id)

	print(subscribed_customers_email)
	send_mail(
	    'Discount Offers From D-Basket',
	    message,
	    'yadyneshdesai30@gmail.com',
	    subscribed_customers_email,
	    fail_silently=False,
	)

	
	return redirect('adminpanel:home')