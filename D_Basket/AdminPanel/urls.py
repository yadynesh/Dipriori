from django.conf.urls import url

from django.contrib.auth.decorators import login_required, permission_required
from . import views,customer_views,item_views,transaction_views,graph_views,discount_views
app_name = 'adminpanel'

urlpatterns = [
   #/emp/customer/list
   url(r'^home', login_required(views.AdminFormView.as_view()) , name='home'),

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
   url(r'^transaction/add/$', login_required(transaction_views.CreateTransaction.as_view()) , name = 'add-transaction'),

   #/emp/transaction/list
   url(r'^transaction/list/$', login_required(transaction_views.TransactionListView.as_view()) , name='list-transactions'),

   #/emp/transaction/<pk>
   url(r'^transaction/(?P<pk>[0-9]+)/$', login_required(transaction_views.UpdateTransaction.as_view()) , name = 'update-transaction'),

   #/emp/transaction/delete/<pk>
   url(r'^transaction/(?P<pk>[0-9]+)/delete/$', login_required(transaction_views.DeleteTransaction.as_view()) , name = 'delete-transaction'),




   url(r'^graph/(?P<type>\w+)/$', login_required(graph_views.graph_main) , name = 'generate-graph'),

   #/emp/graph/bar/<itemset>
   url(r'^graph/bar/(?P<itemset>[0-9]+)/$', login_required(graph_views.barChart) , name = 'generate-barchart'),


   #/emp/discount/list
   url(r'^discount/list/$', login_required(discount_views.DiscountListView.as_view()) , name='list-discounts'),

   #/emp/discount/add
   #url(r'^customer/add/$', login_required(discount_views.CreateDiscount.as_view()) , name = 'add-discount'),

   #/emp/discount/<pk>
   url(r'^discount/(?P<pk>[0-9]+)/$', login_required(discount_views.UpdateDiscount.as_view()) , name = 'update-discount'),

   #/emp/discount/delete/<pk>
   url(r'^discount/(?P<pk>[0-9]+)/delete/$', login_required(discount_views.DeleteDiscount.as_view()) , name = 'delete-discount'),





   #/emp/runclient
   url(r'^runclient/$', login_required(views.runAprioriClient) , name = 'runclient'),



   url(r'^association_rules/list$', login_required(views.AssociationRules.as_view()) , name = 'association_rules'),



   url(r'^discount/sendmail$', login_required(discount_views.sendDiscountMail) , name = 'send-discount-mail'),

  

]