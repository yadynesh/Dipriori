from django.views.generic import View
from django.shortcuts import render,redirect
from .models import Item, Discount, Customer, Configuration
from django.conf import settings
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.mail.backends.smtp import EmailBackend



class DiscountListView(generic.ListView):
	template_name = "AdminPanel/discount_list.html"
	context_object_name = 'discount_list'
	def get_queryset(self):
		return Discount.objects.all()

class UpdateDiscount(generic.UpdateView):
	model = Discount
	fields = ['left_item1', 'left_item2', 'right_item1', 'right_item2' ,'discount_percent']

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
	discount_percent = request.POST['discount_percent']

	conf_object = Configuration.objects.first()
	
	'''
	Configuring the django mail backend to set the username and password.
	This username and password is taken from the Configuration table in dB.
	'''
	backend = EmailBackend(host='smtp.gmail.com', port=587, username=conf_object.admin_email_id, 
                       password=conf_object.admin_email_password, use_tls=True, fail_silently=False)

	#filtering the customers who have subscribed to notifications.
	subscribed_customers = Customer.objects.filter(subscribe=True)
	subscribed_customers_email = []

	for customer in subscribed_customers:
		subscribed_customers_email.append(customer.email_id)

	print(subscribed_customers_email)

	subject, from_email, to = 'Discount Offers From D-Basket', 'popularbasketeer@gmail.com', subscribed_customers_email
	text_content = 'D-BASKET SALE!!!'
	html_mail = get_template("AdminPanel/discount_mail.html")
	mail_context = Context({ 'discount_left': discount_left,'discount_right': discount_right, 'discount_percent': float(discount_percent), })


	msg = EmailMultiAlternatives(subject, text_content, from_email, subscribed_customers_email,connection = backend)

	#rendering the discount_mail.html page with context "mail_context"
	html_content = html_mail.render(mail_context)
	
	msg.attach_alternative(html_content, "text/html")
	msg.send()

	# send_mail(
	#     'Discount Offers From D-Basket',
	#     message,
	#     'D-Basket',
	#     subscribed_customers_email,
	#     fail_silently=False,
	# )

	return redirect('adminpanel:home')