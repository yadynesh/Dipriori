from django import forms #use to tweek what we want to display on the form
from .models import Item,Transaction,Customer,Statistic

class BatchStatisticsForm(forms.Form):
	batch_number = forms.IntegerField(
			label = "Enter batch number",
			widget = forms.NumberInput(
					attrs = {
						"placeholer" : "eg:1",
						"class" : "form-control",
						"min" : "0",
						"max" : Statistic.objects.first().total_batches,
					}
				)
		)

class BatchCompareForm(forms.Form):
	batch_number_1 = forms.IntegerField(
			label = "Enter batch number 1",
			widget = forms.NumberInput(
					attrs = {
						"placeholer" : "eg:1",
						"class" : "form-control",
						"min" : "0",
						"max" : Statistic.objects.first().total_batches,
					}
				)
		)
	batch_number_2 = forms.IntegerField(
			label = "Enter batch number 2",
			widget = forms.NumberInput(
					attrs = {
						"placeholer" : "eg:1",
						"class" : "form-control",
						"min" : "0",
						"max" : Statistic.objects.first().total_batches,
					}
				)
		)