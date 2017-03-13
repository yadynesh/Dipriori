from django.conf.urls import url
from . import views
app_name = 'adminpanel'

urlpatterns = [
   #/emp/customer/list
   url(r'^home', views.AdminFormView.as_view() , name='home'),

   url(r'^customer/list/$', views.IndexView.as_view() , name='list-customers'),

   #/emp/customer/add
   url(r'^customer/add/$', views.CreateCustomer.as_view() , name = 'add-customer'),

	#/emp/customer/<pk>
   url(r'^customer/(?P<pk>[0-9]+)/$', views.UpdateCustomer.as_view() , name = 'update-customer'),

   #/emp/customer/
   #url(r'^customer/(?P<pk>[0-9]+)/details$', views.CustomerDetails.as_view() , name = 'customer-details'),

	#/emp/customer/delete/<pk>
   url(r'^customer/(?P<pk>[0-9]+)/delete/$', views.DeleteCustomer.as_view() , name = 'delete-customer'),


]