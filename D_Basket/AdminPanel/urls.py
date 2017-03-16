from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from . import views
app_name = 'adminpanel'

urlpatterns = [
   #/emp/customer/list
   url(r'^home', views.AdminFormView.as_view() , name='home'),

   url(r'^customer/list/$', login_required(views.CustomerListView.as_view()) , name='list-customers'),

   #/emp/customer/add
   url(r'^customer/add/$', login_required(views.CreateCustomer.as_view()) , name = 'add-customer'),

	#/emp/customer/<pk>
   url(r'^customer/(?P<pk>[0-9]+)/$', login_required(views.UpdateCustomer.as_view()) , name = 'update-customer'),

   #/emp/customer/
   #url(r'^customer/(?P<pk>[0-9]+)/details$', views.CustomerDetails.as_view() , name = 'customer-details'),

	#/emp/customer/delete/<pk>
   url(r'^customer/(?P<pk>[0-9]+)/delete/$', login_required(views.DeleteCustomer.as_view()) , name = 'delete-customer'),


]