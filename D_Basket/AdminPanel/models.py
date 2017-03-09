from django.db import models

# Create your models here.

class Admin(models.Model):
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)

	def __str__(self):
		return self.username

class Customer(models.Model):
	name = models.CharField(max_length = 100)
	email_id = models.CharField(max_length = 40)
	subscribe = models.BooleanField(default = False)

	def __str__(self):
		return self.name + "-" + self.email_id + "-" + str(self.subscribe)


class Item(models.Model):
	item_name = models.CharField(max_length = 50)

	def __str__(self):
		return str(self.pk) + "-"+ self.item_name


class Transaction(models.Model):

	trans_id = models.IntegerField()
	cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	item_id = models.ForeignKey(Item, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.trans_id) + "-" + str(self.cust_id) + "-" + str(self.id)