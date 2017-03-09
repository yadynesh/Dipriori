from django.conf.urls import url
from . import views
app_name = 'adminpanel'

urlpatterns = [

   #emp/customer/add
   url(r'^customer/add/$', views.CustomerCreate.as_view() , name = 'add-customer'),
]