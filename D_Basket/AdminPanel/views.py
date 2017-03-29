from django.views.generic import View
from django.shortcuts import render,redirect
import matplotlib
import pandas as pd
from .models import Item, Discount
from django.conf import settings


class AdminFormView(View):
	def get(self, request, *args, **kwargs):
		template = "AdminPanel/home.html"
		return render(request, template,)

def runAprioriClient(request):
    from . import AprioriClient
    template = "AdminPanel/home.html"
    return render(request, template,)


class AssociationRules(View):

    def get(self, request, *args, **kwargs):
        association_rules = pd.read_csv(settings.BASE_DIR+"/association_rules.csv")
        print(association_rules)
        template = "AdminPanel/association_rules.html"
        return render(request, template,{'association_rules':association_rules})


    def post(self, request, *args, **kwargs):
        print(request.POST['ass_left'])

        left_items = request.POST['ass_left'].split(",")  
        left_item1 = Item.objects.get(item_name = left_items[0])
        left_item2 = None
        if(len(left_items) == 2):
            left_item2 = Item.objects.get(item_name = left_items[1])

        right_items = request.POST['ass_right'].split(",")  
        right_item1 = Item.objects.get(item_name = right_items[0])
        right_item2 = None
        if(len(right_items) == 2):
            right_item2 = Item.objects.get(item_name = right_items[1])

        confidence = request.POST['confidence']

        discount = Discount(left_item1 = left_item1,left_item2 = left_item2,right_item1 = right_item1,right_item2 = right_item2,confidence = confidence)
        discount.save()

        return redirect('adminpanel:list-discounts')



