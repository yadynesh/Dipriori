from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import View
from .models import Customer
from django.core.urlresolvers import reverse_lazy

# from django.contrib.auth import authenticate,login 
#from .forms import AdminForm
#authenticate takes username and passoword and verifies it in database and login is for session

#Create your views here.
#

class CustomerListView(generic.ListView):
	template_name = "AdminPanel/customer_list.html"
	context_object_name = 'customer_list'
	def get_queryset(self):
		return Customer.objects.all()

class CreateCustomer(generic.CreateView):
	model = Customer
	fields = ['first_name', 'last_name', 'email_id', 'subscribe']
	
class UpdateCustomer(generic.UpdateView):
	model = Customer
	fields = ['first_name', 'last_name', 'email_id', 'subscribe']

class DeleteCustomer(generic.DeleteView):
	model = Customer
	success_url = reverse_lazy('adminpanel:list-customers')

class CustomerDetails(generic.DetailView):
	model = Customer
	template_name = "AdminPanel/customer-details.html"




class AdminFormView(View):

	
	def get(self, request, *args, **kwargs):
		template = "AdminPanel/home.html"
		return render(request, template,)


# 	def post(self, request, *args, **kwargs):
# 		template = "AdminPanel/registration_form.html"
# 		admin_form = AdminForm(request.POST)
# 		context={
# 			'form':admin_form
# 		}

# 		if admin_form.is_valid():
# 			user = admin_form.save(commit = False)

# 			username = admin_form.cleaned_data["username"]
# 			password = admin_form.cleaned_data['password']
# 			print(password)
# 			user.set_password(password)

# 			user.save()
# 			user = authenticate(username = username, password = password)

# 			if user is not None:
# 				if user.is_active:
# 					print("user active")
# 					login(request, user)
# 					return redirect('adminpanel:list-customers')
# 		return render(request,template,context)