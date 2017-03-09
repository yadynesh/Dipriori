from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Admin(models.Model):
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)

	def __str__(self):
		return self.username

class Customer(models.Model):
	name = models.CharField(max_length = 100, verbose_name = 'Customer Name')
	email_id = models.EmailField(max_length = 40, verbose_name = 'Email address')
	subscribe = models.BooleanField(default = False)

	def __str__(self):
		return self.name + "-" + self.email_id + "-" + str(self.subscribe)

	def get_absolute_url(self):
		return reverse('adminpanel:add-customer')


class Item(models.Model):
	item_name = models.CharField(max_length = 50, verbose_name = 'Item Name')

	def __str__(self):
		return str(self.pk) + "-"+ self.item_name


class Transaction(models.Model):

	trans_id = models.IntegerField(verbose_name = 'Transaction ID')
	cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = 'Customer ID')
	item_id = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name = 'Item ID')

	def __str__(self):
		return str(self.trans_id) + "-" + str(self.cust_id) + "-" + str(self.id)