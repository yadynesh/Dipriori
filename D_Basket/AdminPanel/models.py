from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.

# class Admin(models.Model):
# 	username = models.CharField(max_length = 20)
# 	password = models.CharField(max_length = 20)
# 	first_name = models.CharField(max_length = 100, verbose_name = 'First Name')
# 	last_name = models.CharField(max_length = 100, verbose_name = 'Last Name')
# 	email_id = models.EmailField(max_length = 100, verbose_name = 'Email address')

# 	def __str__(self):
# 		return self.username

class Customer(models.Model):
	first_name = models.CharField(max_length = 100,null = False, blank=False, verbose_name = 'First Name')
	last_name = models.CharField(max_length = 100,null = False, blank=False, verbose_name = 'Last Name')
	email_id = models.EmailField(max_length = 100,null = False, blank=False, verbose_name = 'Email address')
	join_date = models.DateTimeField(default = timezone.now, editable = False)
	last_modified = models.DateTimeField(auto_now = True)
	subscribe = models.BooleanField(default = False, verbose_name = 'Subscribed')

	def __str__(self):
		return  self.first_name + " " + self.last_name + "-" + str(self.pk) + "-" + self.email_id + "-" + str(self.subscribe)


	def get_absolute_url(self):
		return reverse('adminpanel:list-customers')


class Item(models.Model):
	item_name = models.CharField(max_length = 50, verbose_name = 'Item Name')
	stocks = models.IntegerField()

	def __str__(self):
		return str(self.pk) + "-"+ self.item_name

	def get_absolute_url(self):
		return reverse('adminpanel:list-items')


class Transaction(models.Model):
	trans_id = models.IntegerField(default = 1,verbose_name = 'Transaction ID')
	cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name = 'Customer ID')
	item_id = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name = 'Item ID')

	def __str__(self):
		return str(self.trans_id) + "-" + str(self.cust_id) + "-" + str(self.id)

	def get_absolute_url(self):
		return reverse('adminpanel:list-transactions')


class Discount(models.Model):
	left_item1 = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name = 'Item', blank=True, null=True, related_name = 'left_item1')
	left_item2 = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name = 'Item', blank=True, null=True, related_name = 'left_item2')
	right_item1 = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name = 'Item', blank=True, null=True, related_name = 'right_item1')
	right_item2 = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name = 'Item', blank=True, null=True, related_name = 'right_item2')
	confidence = models.FloatField()

	def __str__(self):
		return  str(self.left_item1) + " " + str(self.left_item2) + "--->" + str(self.right_item1) + " " + str(self.right_item2)

	def get_absolute_url(self):
		return reverse('adminpanel:list-discounts')

		

