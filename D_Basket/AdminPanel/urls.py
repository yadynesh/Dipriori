from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from . import views,customer_views,item_views,transaction_views
app_name = 'adminpanel'

urlpatterns = [
   #/emp/customer/list
   url(r'^home', views.AdminFormView.as_view() , name='home'),

   url(r'^customer/list/$', login_required(customer_views.CustomerListView.as_view()) , name='list-customers'),

   #/emp/customer/add
   url(r'^customer/add/$', login_required(customer_views.CreateCustomer.as_view()) , name = 'add-customer'),

	#/emp/customer/<pk>
   url(r'^customer/(?P<pk>[0-9]+)/$', login_required(customer_views.UpdateCustomer.as_view()) , name = 'update-customer'),

	#/emp/customer/delete/<pk>
   url(r'^customer/(?P<pk>[0-9]+)/delete/$', login_required(customer_views.DeleteCustomer.as_view()) , name = 'delete-customer'),

   #/emp/customer/
   #url(r'^customer/(?P<pk>[0-9]+)/details$', views.CustomerDetails.as_view() , name = 'customer-details'),
  


  
   #/emp/item/list
    url(r'^item/list/$', login_required(item_views.ItemListView.as_view()) , name='list-items'),

   #/emp/item/add
   url(r'^item/add/$', login_required(item_views.CreateItem.as_view()) , name = 'add-item'),

   #/emp/item/<pk>
   url(r'^item/(?P<pk>[0-9]+)/$', login_required(item_views.UpdateItem.as_view()) , name = 'update-item'),

   #/emp/item/delete/<pk>
   url(r'^item/(?P<pk>[0-9]+)/delete/$', login_required(item_views.DeleteItem.as_view()) , name = 'delete-item'),




   #/emp/transaction/add/
   url(r'^transactions/add/$', login_required(transaction_views.CreateTransaction.as_view()) , name = 'add-transaction'),

]